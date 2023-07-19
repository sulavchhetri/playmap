"""
    This is the init file where the logger is setup
"""

from loguru import logger as log


def loguru_setup(logfile="logfile.log"):
    """
        This function firstly removes the existing log file for clean start
        and then create a log file with custom config and return it
    """
    log.remove()
    log.add(
        logfile,
        colorize=True,
        format="{name} | {message}",
        level="INFO",
        mode="w"
    )
    return log


logger = loguru_setup()
