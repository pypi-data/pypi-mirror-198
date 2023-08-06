#!/usr/bin/env python3

"""
Enable Pipeline.

Argument handling for the 'pipelines' subcommand option '--enable-pipeline'
"""

import logging

import json

from codestream.cli.args import CONSOLE_PARSER
from codestream.common import config, logger, rest, VRASettings, whoami
from codestream.api.codestream import pipeline

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------


def run(bearer_token=None, name=None, project=None, settings=VRASettings):
    """
    Run.

    Returns:
        result: Boolean True for success, False for Failure.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # The name and project are mandatory.
    if name is None or project is None:
        CONSOLE_PARSER.print_help()
        message = "You need to provide a project and name."
        log.error(message)
        logger.eprint(message)
        return False

    try:
        (
            response_json,
            status_code,
        ) = pipeline.enable_pipeline(
            settings=settings,
            bearer_token=bearer_token,
            name=name,
            project=project,
        )

    except Exception as err:
        message = f"An exception occurred while enabling pipeline {name} in project {project}."
        log.error(message)
        log.error(err)
        return False

    if config.TRACE_ENABLED:
        log.debug(json.dumps(response_json, indent=4))

    result = rest.check_status_code(status_code)

    return result
