# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import os
import pickle
import random
import time
import typing as t
import threading as th
from abc import ABC, abstractmethod
from collections import deque, OrderedDict
from dataclasses import dataclass

import pkg_resources

from . import AppIndicator, Gtk
from .. import APP_NAME
from ..shared import ShutdownableThread, SocketClient, get_logger, SocketMessage

DT = t.TypeVar("DT")


@dataclass(frozen=True)
class _MenuItemConfig:
    label: str
    sensitive: bool = True
    separator_before: bool = False


@dataclass
class _State:
    active = False

    @abstractmethod
    def click(self):
        ...


@dataclass
class _StaticState(_State):
    callback: t.Callable = None

    def click(self):
        if self.callback:
            self.callback()


@dataclass
class _BoolState(_StaticState):
    value: bool = True

    def __bool__(self):
        return self.value

    @property
    def active(self) -> bool:
        return self.value

    def click(self):
        self.value = not self.value
        super().click()


class _BaseIndicator(ShutdownableThread, t.Generic[DT], ABC):
    SOCKRCV_INTERVAL_SEC = 1.0
    RENDER_INTERVAL_SEC = 1.0
    RENDER_ERROR_TIMEOUT_SEC = 5.0

    def __init__(
        self,
        indicator_name: str,
        socket_topic: str = None,
        icon_name_default: str = None,
        icon_path_dynamic_tpl: str = None,
        icon_thresholds: list[int] = None,
        label: str = None,
    ):
        super().__init__(command_name=indicator_name, thread_name="ui")
        self._timeout_sec = 0.0
        self._warning_switch = False

        self._monitor_data_buf = deque[bytes](maxlen=1)
        self._socket_client_pause = th.Event()
        self._socket_client_ready = th.Event()
        self._socket_client = SocketClient(
            self._monitor_data_buf,
            eff_recv_interval_sec=self.SOCKRCV_INTERVAL_SEC,
            pause_event=self._socket_client_pause,
            ready_event=self._socket_client_ready,
            socket_topic=socket_topic or indicator_name,
            command_name=indicator_name,
        )

        self._theme_path = pkg_resources.resource_filename("es7s", "data/icons-v7")
        self._icon_name_default = icon_name_default
        self._icon_path_dynamic_tpl = icon_path_dynamic_tpl
        self._icon_thresholds = icon_thresholds

        self._hidden = _BoolState(value=False, callback=self._update_visibility)
        self._state_map = OrderedDict[_MenuItemConfig, _State]()
        self._state_map.update(
            {_MenuItemConfig(label or indicator_name, False, True): _StaticState()}
        )
        self._init_state()
        self._state_map.update({_MenuItemConfig("Hide", True, True): self._hidden})

        self._indicator: AppIndicator.Indicator = AppIndicator.Indicator.new(
            f"es7s-indicator-{indicator_name}",
            self._icon_name_default or "apport-symbolic",
            AppIndicator.IndicatorCategory.APPLICATION_STATUS,
        )
        self._indicator.set_attention_icon("dialog-warning")
        self._indicator.set_icon_theme_path(self._theme_path)

        self._menu = Gtk.Menu()
        self._init_menu()
        self._menu.show()
        self._indicator.set_menu(self._menu)
        self._update_visibility()

        self._socket_client.start()
        self.start()

    def _init_state(self):
        pass

    def _init_menu(self):
        for config, state in self._state_map.items():
            self._make_menu_item(config, state)

    def _make_menu_item(self, config: _MenuItemConfig, state: _State = None) -> Gtk.CheckMenuItem:
        if config.separator_before:
            sep = Gtk.SeparatorMenuItem.new()
            sep.show()
            self._menu.append(sep)

        item = Gtk.CheckMenuItem.new_with_label(config.label)
        item.set_active(state.active)
        item.set_sensitive(config.sensitive)
        item.connect("activate", lambda c=config: self._click_menu_item(config))
        item.show()
        self._menu.append(item)

        return item

    def _click_menu_item(self, config: _MenuItemConfig):
        if (state := self._state_map.get(config)) is not None:
            state.click()

    def _update_visibility(self):
        if self._hidden:
            self._indicator.set_status(AppIndicator.IndicatorStatus.PASSIVE)
        else:
            self._indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)

    def run(self):
        super().run()
        self._socket_client_ready.wait(0.1)

        while True:
            if self.is_shutting_down():
                self.destroy()
                break
            if self._timeout_sec > 0.1:
                self._sleep(0.1)
                continue
            self._sleep(self._timeout_sec)
            self._update()

    def _sleep(self, timeout_sec: float):
        if timeout_sec == 0:
            return
        time.sleep(timeout_sec)
        self._timeout_sec = max(0.0, self._timeout_sec - timeout_sec)

    def _add_timeout(self, timeout_sec: float = None):
        self._timeout_sec += timeout_sec or self.RENDER_INTERVAL_SEC

    def _update(self):
        logger = get_logger()

        try:
            try:
                msg_raw = self._monitor_data_buf[0]
            except IndexError:
                logger.warning("No data from daemon")
                self._add_timeout()
                self._render_no_data()
                return

            msg = self._deserialize(msg_raw)

            # msg_ttl = self._setup.message_ttl
            msg_ttl = 5.0  # @TODO
            now = time.time()

            if now - msg.timestamp > msg_ttl:
                self._monitor_data_buf.remove(msg_raw)
                raise RuntimeError(f"Expired socket message: {now} > {msg.timestamp}")

            else:
                logger.trace(msg_raw, label="Received data dump")
                logger.debug("Deserialized changed message: " + repr(msg))
                self._add_timeout()
                self._render(msg)

        except Exception as e:
            logger.exception(e)
            self._add_timeout(self.RENDER_ERROR_TIMEOUT_SEC)
            self._render_error()

    def _deserialize(self, msg_raw: bytes) -> SocketMessage[DT]:
        msg = pickle.loads(msg_raw)
        return msg

    def _select_icon(self, carrier_value: float) -> str:
        if not self._icon_thresholds or not self._icon_path_dynamic_tpl:
            return self._icon_name_default

        icon_subtype = self._icon_thresholds[-1]
        for thr in self._icon_thresholds:
            icon_subtype = thr
            if carrier_value >= thr:
                break
        return self._icon_path_dynamic_tpl % icon_subtype

    @abstractmethod
    def _render(self, msg: SocketMessage[DT]):
        ...

    def _render_no_data(self):
        self._set("...", None, AppIndicator.IndicatorStatus.ACTIVE)

    def _render_result(
        self, result: str, guide: str = None, warning: bool = False, icon: str = None
    ):
        self._warning_switch = not self._warning_switch
        status = AppIndicator.IndicatorStatus.ACTIVE
        if warning and self._warning_switch:
            status = AppIndicator.IndicatorStatus.ATTENTION
        self._set(result, guide, status)

        if icon:
            self._indicator.set_icon(os.path.join(self._theme_path, icon))

    def _render_error(self):
        self._set("ERR", None, AppIndicator.IndicatorStatus.ATTENTION)

    def _set(self, label: str, guide: str | None, status: AppIndicator.IndicatorStatus):
        if self._hidden:
            return
        self._indicator.set_label(label, guide or label)
        self._indicator.set_status(status)
