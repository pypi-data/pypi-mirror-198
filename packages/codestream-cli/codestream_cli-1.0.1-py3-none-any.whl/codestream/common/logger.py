#!/usr/bin/env python3

"""
Log module.

Logging related functions.
"""

import os
import sys
import logging
import logging.config

from codestream.common import config

#########################
# Functions
#########################


def eprint(*args, **kwargs):
    """
    eprint.

    Prints a message to stderr instead of stdout
    """
    print(*args, file=sys.stderr, **kwargs)


def setup(name):
    """
    Logger setup.

    Sets up a global logger based on the environment variable LOGLEVEL
    """
    levels_allowed = [
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
    ]
    try:
        # Read a default log level from the environment.
        loglevel = os.getenv("CODESTREAM_CLI_LOG_LEVEL", "WARNING").upper()

        # Check if a log file has been specified.
        logfile = os.getenv("CODESTREAM_CLI_LOG_FILE", None)

        # Only setup the logger if a correct level was provided.
        if not loglevel.upper() in levels_allowed:
            joined_levels_allowed = ", ".join(levels_allowed)
            message = (
                f"The provided log level '{loglevel}' is not permitted.\n"
                f"Please select from {joined_levels_allowed}"
            )
            eprint(message)
            raise Exception

        # TODO: Move to newer method of using config file.
        # logging.config.fileConfig('config.yaml')

        logging.getLogger(name)

        if logfile is not None:
            if config.TRACE_ENABLED:
                eprint(f"Writing logs to file {logfile}")

            logging.basicConfig(
                format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
                datefmt="%Y-%m-%d %I:%M:%S %p",
                level=loglevel,
                filename=logfile,
                filemode="a",
            )

        else:
            if config.TRACE_ENABLED:
                eprint("Writing logs to stderr stream")

            logging.basicConfig(
                format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
                datefmt="%Y-%m-%d %I:%M:%S %p",
                level=loglevel,
                stream=sys.stderr,
            )

    except Exception as err:
        eprint(err)
        raise Exception from err

    return 0
