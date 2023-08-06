#!/usr/bin/env python3

"""
Codestream.

A collection of command-line utilities for working with vRA.
"""

import logging

from codestream.common import logger
from codestream.cli import command

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------


def main():
    """
    Start main.

    Main is used for starting from tests and from the CLI.
    """
    try:
        logger.setup(__name__)

    except Exception as err:
        logger.eprint("Failed to setup logger, aborting execution.")
        raise SystemExit(1) from err

    log.debug("Launching CLI")
    raise SystemExit(command.entrypoint())
