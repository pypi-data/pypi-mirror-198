#!/usr/bin/env python3

"""
Validate Pipeline.

Argument handling for the 'pipelines' subcommand option '--validate-pipeline'
"""

import logging
from pathlib import Path

from codestream.cli.args import CONSOLE_PARSER
from codestream.common import config, logger, files, whoami
from codestream.api.codestream import pipeline

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------


def run(file=None):
    """
    Run.

    Returns:
        int: Result code 0 or 1
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # The filename is mandatory.
    if file is None:
        CONSOLE_PARSER.print_help()
        log.error("You need to provide a filename.")
        return False

    # Make sure the file exists.
    try:
        file_path = Path(files.get_full_path(path=file))

        if file_path.is_file():
            log.debug("The file exists at path %s", file_path)
        else:
            message = (
                f"The provided file does not exist at the location {file_path}"
            )
            log.error(message)
            logger.eprint(message)
            return False

    except FileExistsError as err:
        message = f"File exists error at path {file_path}"
        log.error(message)
        log.error(err)
        return False

    except Exception as err:
        message = f"Unhandled exception checking for file {file_path}"
        log.error(message)
        log.error(err)
        return False

    # Read the YAML contents.
    try:
        pipeline_yaml = files.read_yaml_file(file_path)

    except Exception as err:
        message = (
            f"An exception occurred while reading YAML pipeline {file_path}"
        )
        log.error(message)
        log.error(err)
        return False

    # Ensure that the YAML file is valid Code Stream.
    try:
        pipeline_spec, result = pipeline.validate_pipeline(
            pipeline_yaml=pipeline_yaml,
        )

    except Exception as err:
        message = f"An exception occurred while validating YAML from file {file_path}"
        log.error(message)
        log.error(err)
        return False

    if result:
        # Double check that both the name and project are populated.
        if not pipeline_spec.get("name") or not pipeline_spec.get("project"):
            message = f"Failed to extract the mandatory fields (name,project) from {file_path}"
            log.error(message)
            return False

        # Extract the pipeline name and project from the YAML.
        name = pipeline_spec["name"]
        project = pipeline_spec["project"]

    else:
        message = f"Pipeline validation failed for file {file_path}"
        log.error(message)
        return False

    message = (
        f"Pipeline validation complete for Name: {name} Project: {project}"
    )
    log.info(message)

    return True
