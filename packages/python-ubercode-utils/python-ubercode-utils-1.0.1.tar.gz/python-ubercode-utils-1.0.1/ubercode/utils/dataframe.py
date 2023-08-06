""" common utilities for working with dataframes"""
from typing import Any
from . import logging


# extend the logging to include log.dataframe()
# NOTE: making dataframe type Any, so we don't have to include pandas but intended use is dataframe
# todo: decide if better to include in different install requiring pandas like the requests utils version
class DataframeLogger(logging.ColorLogger):
    def dataframe(self, dataframe: Any,  label: str = None, color: str = "ALWAYS") -> None:
        if label:
            self.info(label)
        color = DataframeLogger.DEFAULT_COLOR_MAP.get(color, DataframeLogger.DEFAULT_COLOR_MAP["ALWAYS"])
        self.log(dataframe, log_level="ALWAYS", color=color)
