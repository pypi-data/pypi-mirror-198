# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------

from ._base import _BaseIndicator, _BoolState, _MenuItemConfig
from ..shared import SocketMessage
from ..shared.dto import ShocksInfo
import pytermor as pt


class IndicatorShocks(_BaseIndicator):
    def __init__(self):
        self._show_lat = _BoolState(value=False)

        super().__init__(
            "shocks",
            icon_name_default="shocks.svg",
            icon_path_dynamic_tpl="shocks-%s.svg",
            icon_thresholds=[
                90,
                80,
                70,
                50,
                30,
                10,
                0,
            ],
        )

    def _init_state(self):
        self._state_map.update({
            _MenuItemConfig("Latency (sec)"): self._show_lat,
        })

    def _render(self, msg: SocketMessage[ShocksInfo]):
        result = self._format_result(msg.data)
        icon_subtype = self._get_icon_subtype(msg.data)
        icon = self._icon_path_dynamic_tpl % icon_subtype
        self._render_result(result, icon=icon)

    def _format_result(self, data: ShocksInfo) -> str:
        if not self._show_lat:
            return ""
        if not data.latency_s:
            return "--"
        return pt.format_time_ms(data.latency_s*1e3)

    # noinspection PyMethodMayBeStatic
    def _get_icon_subtype(self, data: ShocksInfo) -> str:
        if not data.running:
            return "down"
        if not data.healthy:
            return "failure"
        return "up"
