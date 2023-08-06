#!/usr/bin/env python3

"""
Blueprint module.

A collection of functions for working with blueprints.
"""

import logging

from codestream.common import config, whoami

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------


def lint(settings, file):
    """
    Lint blueprint.

    Checks a vRA Blueprint YAML file for errors.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # TODO: Finish this.
    print(settings)
    print(file)

    return 0
