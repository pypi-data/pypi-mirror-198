# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2022-2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import os
import signal
import sys

from . import Gtk
from .indicator_cpu_load import IndicatorCpuLoad
from .indicator_memory import IndicatorMemory
from .indicator_temperature import IndicatorTemperature
from .. import APP_TRACE
from ..shared import (
    get_stdout,
    init_logger,
    LoggerParams,
    init_io,
    IoParams,
    init_config,
    get_stderr,
    get_logger,
    shutdown_started,
    shutdown_threads,
)
from ..shared.config import ConfigLoaderParams
from ..shared.threads import exit_gracefully


def invoke():
    os.environ.update({"ES7S_DOMAIN": "GTK"})
    _init()
    try:
        ic = IndicatorController()
        ic.run()
    except SystemExit:
        if stdout := get_stdout(False):
            stdout.echo()
        raise


def _init():
    logger_params = LoggerParams()
    if APP_TRACE:
        logger_params.verbosity = 3
    io_params = IoParams()

    logger = init_logger(params=logger_params)
    _, _ = init_io(io_params)
    init_config(ConfigLoaderParams())

    logger.log_init_params(
        ("Log configuration:", logger_params),
        ("Logger setup:", {"handlers": logger.handlers}),
        ("IO configuration:", io_params),
        ("Stdout proxy setup:", get_stdout().as_dict()),
        ("Stderr proxy setup:", get_stderr().as_dict()),
    )


class IndicatorController:
    def __init__(self):
        signal.signal(signal.SIGINT, self._exit)
        signal.signal(signal.SIGTERM, self._exit)

        self._indicators = [
            # IndicatorDatetime(),
            IndicatorTemperature(),
            IndicatorCpuLoad(),
            IndicatorMemory(),
        ]

    def run(self):
        Gtk.main()
        for indicators in self._indicators:
            indicators.join()

    def _exit(self, signal_code: int, *args):
        exit_gracefully(signal_code, callback=None)
        Gtk.main_quit()
        sys.exit(signal_code)
