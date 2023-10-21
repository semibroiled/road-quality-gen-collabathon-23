"""This module configures logging parameters for the project"""

# Type hinting
# from pathlib import Path
# from pandas import DataFrame

# Local Modules
# moved here

# CI/CD
# from functools import lru_cache
# import sys, os
import logging
from logging import Logger

# Put Local Module in path
# root_directory_module = os.path.abspath(os.path.join(os.path.curdir, "localpack"))
# sys.path.append(root_directory_module)

# Import time
# import time


# Setup Module Level Logging for our Running Application
def logger(filename: __name__, /, log_in_file=True, log_in_stream=True) -> Logger:
    # TODO: Add Docstring
    # TODO: Add customisable params in sep file
    # TODO: periodically delete logs
    # Set Instance of Logging for file
    log = logging.getLogger(filename)

    # Set Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s", "", "%"
    )

    if log_in_stream:
        # Set Stream Handler instance and add formatter
        # This outputs text to the terminal
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        # sh.setLevel(logging.DEBUG)
    log.addHandler(sh)

    if log_in_file:
        # Set Filehandler instance and formatter
        # This creates a file where the logged data is stored
        # By default, mode is a, encoding is None, delay is False
        fh = logging.FileHandler(f"./utils/log/{filename}_history.log", mode="a")
        fh.setFormatter(formatter)
        # fh.setLevel(logging.DEBUG)
        log.addHandler(fh)

    # Set Logging Level
    log.setLevel(logging.DEBUG)

    return log
