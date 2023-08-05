# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------

from pytermor import format_auto_float

from ._base import _BaseIndicator
from ..shared import SocketMessage
from ..shared.dto import CpuInfo


class IndicatorCpuLoad(_BaseIndicator[CpuInfo]):
    def __init__(self):
        super().__init__(
            "cpu-load",
            "cpu",
            icon_name_default="cpuload-0.svg",
            icon_path_dynamic_tpl="cpuload-%d.svg",
            icon_thresholds=[
                99,
                90,
                75,
                50,
                25,
                0,
            ],
        )

    def _render(self, msg: SocketMessage[CpuInfo]):
        self._render_result(
            self._format_result(msg.data.load_perc, *msg.data.load_avg),
            self._format_result(100, *[16.16] * len(msg.data.load_avg)),
            icon=self._select_icon(msg.data.load_perc),
        )

    def _format_result(self, perc: float, *avg: float) -> str:
        return f"{perc:^3.0f}%  " + " ".join(format_auto_float(a, 4) for a in avg)
