# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
from ._base import _BaseIndicator
from ..shared import SocketMessage
from ..shared.dto import TemperatureInfo


class IndicatorTemperature(_BaseIndicator[TemperatureInfo]):
    def __init__(self):
        super().__init__(
            "temperature",
            icon_name_default="temperature-0.svg",
            icon_path_dynamic_tpl="temperature-%d.svg",
            icon_thresholds=[
                90,
                70,
                50,
                30,
                15,
                5,
            ],
        )

    def _render(self, msg: SocketMessage[TemperatureInfo]):
        orig_values = msg.data.values_c
        sorted_values = sorted(orig_values, key=lambda v: v[1], reverse=True)

        max_value = 0
        if len(sorted_values) > 0:
            max_value = sorted_values[0][1]

        values_limit = 1  # @TODO to config
        top_values_origin_indexes = []
        for (k, v) in sorted_values[:values_limit]:
            top_values_origin_indexes.append(orig_values.index((k, v)))

        values_str = []
        guide = []
        warning = False
        for oindex in sorted(top_values_origin_indexes):
            _, val = orig_values[oindex]
            if val > 90:  # @TODO to config
                warning = True
            val_str = str(round(val)).rjust(2)
            values_str.append(val_str)
            guide.append("1" + val_str[-2:])

        self._render_result(
            self._format_result(*values_str),
            self._format_result(*guide),
            warning,
            icon=self._select_icon(max_value),
        )

    def _format_result(self, *result: str) -> str:
        return " ".join([*result, "°C"])
