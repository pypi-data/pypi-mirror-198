# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import typing as t
from pytermor import format_auto_float

from ._base import _BaseIndicator, _MenuItemConfig, _BoolState, _State
from ..shared import SocketMessage
from ..shared.dto import CpuInfo


class IndicatorCpuLoad(_BaseIndicator[CpuInfo]):
    def __init__(self):
        self._show_perc = _BoolState(value=True)
        self._show_avg = _BoolState(value=False)

        super().__init__(
            "cpu-load",
            "cpu",
            icon_name_default="cpuload-0.svg",
            icon_path_dynamic_tpl="cpuload-%d.svg",
            icon_thresholds=[
                85,
                87,
                75,
                62,
                50,
                37,
                25,
                12,
                0,
            ],
            label="CPU load",
        )

    def _init_state(self, state_map: t.Mapping[_MenuItemConfig, _State] = None):
        self._state_map.update(
            {
                _MenuItemConfig("Current (%)"): self._show_perc,
                _MenuItemConfig("Average (1/5/15min)"): self._show_avg,
            }
        )

    def _render(self, msg: SocketMessage[CpuInfo]):
        self._render_result(
            self._format_result(msg.data.load_perc, *msg.data.load_avg),
            self._format_result(100, *[16.16] * len(msg.data.load_avg)),
            icon=self._select_icon(msg.data.load_perc),
        )

    def _format_result(self, perc: float, *avg: float) -> str:
        parts = []
        if self._show_perc.active:
            parts += [f"{perc:3.0f}% "]
        if self._show_avg.active:
            parts += (format_auto_float(a, 4) for a in avg)
        return " ".join(parts)
