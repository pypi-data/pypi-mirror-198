#!/usr/bin/env python3

"""
Export Pipelines.

Argument handling for the 'pipelines' subcommand option '--export-pipeline'
"""

import logging
import os

import json

from codestream.cli.args import CONSOLE_PARSER
from codestream.common import config, files, logger, rest, VRASettings, whoami
from codestream.api.codestream import pipeline

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------


def run(
    bearer_token=None, name=None, project=None, file=None, settings=VRASettings
):
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

    # Before exporting, check if the pipeline actually exists.
    try:
        log.debug(
            "Checking if pipeline %s exists in project %s", name, project
        )

        (
            response_json,
            status_code,
        ) = pipeline.check_pipeline(
            settings=settings,
            bearer_token=bearer_token,
            name=name,
            project=project,
        )

    except Exception as err:
        message = f"An exception occurred whilst checking pipeline {name}."
        log.error(message)
        log.error(err)
        return False

    if config.TRACE_ENABLED:
        log.debug(json.dumps(response_json, indent=4))

    if status_code == 200:
        message = f"A pipeline named {name} in project {project} exists and will be exported."
        log.debug(message)
        export_pipeline = True

    elif status_code == 404:
        message = f"No pipeline named {name} was found in project {project}"
        log.error(message)
        logger.eprint(message)
        return False

    else:
        message = f"Failed to determine whether the pipeline named {name} exists in project {project}"
        log.error(message)
        logger.eprint(message)
        return False

    if export_pipeline:
        message = f"Exporting pipeline {name} in project {project}"
        log.debug(message)

        try:
            (
                response_yaml,
                status_code,
            ) = pipeline.export_pipeline(
                settings=settings,
                bearer_token=bearer_token,
                name=name,
                project=project,
            )

        except Exception as err:
            message = f"An exception occurred while exporting pipeline {name}."
            log.error(message)
            log.error(err)
            return False

        if config.TRACE_ENABLED:
            log.debug(response_yaml)

        # No point writing to screen or file if it failed.
        if status_code != 200:
            message = f"Failed to export pipeline {name} in project {project}"
            log.error(message)
            logging.error(message)
            return False

        # If a file was provided, the response is written to it.
        if file:
            if settings.dry_run:
                message = "Skipping write to file as dry run is enabled."
                log.debug(message)

            else:
                # Write the response to a file on disk.
                files.write_yaml_file(contents=response_yaml, file=file)
                if not os.path.exists(file):
                    log.error("Failed to write pipeline to file %s", file)
                    return False

        # If no file was provided, print the response to stdout.
        else:
            print(response_yaml)

    result = rest.check_status_code(status_code)

    return result
