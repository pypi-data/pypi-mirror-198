#!/usr/bin/env python3

"""
Import Pipelines.

Argument handling for the 'pipelines' subcommand option '--import-pipeline'
"""

import logging
from pathlib import Path

import json

from codestream.cli.args import CONSOLE_PARSER
from codestream.common import config, files, logger, rest, VRASettings, whoami
from codestream.api.codestream import pipeline

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------


def run(bearer_token=None, file=None, settings=VRASettings):
    """
    Run.

    Returns:
        result: Boolean True for success, False for failure.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # The filename is mandatory.
    if file is None:
        CONSOLE_PARSER.print_help()
        message = "You need to provide a filename."
        log.error(message)
        logger.eprint(message)
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
            f"An exception occurred while reading YAML pipeline {file_path}."
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
        message = f"An exception occurred while validating YAML from file {file_path}."
        log.error(message)
        log.error(err)
        return False

    if result:
        # Double check that both the name and project are populated.
        if not pipeline_spec.get("name") or not pipeline_spec.get("project"):
            message = f"Failed to extract the mandatory fields (name,project) from {file_path}"
            logger.eprint(message)
            log.error(message)
            return 1

        # Extract the pipeline name and project from the YAML.
        name = pipeline_spec["name"]
        project = pipeline_spec["project"]

    else:
        message = f"Pipeline validation failed for file {file_path}"
        log.error(message)
        return 1

    # Before importing, check if the pipeline already exists.
    try:
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
        raise Exception from err

    if config.TRACE_ENABLED:
        log.debug(json.dumps(response_json, indent=4))

    if settings.dry_run:
        message = f"Dry run enabled, skipping check for pipeline {name} in project {project}."
        log.debug(message)
        import_type = "disabled"

    elif status_code == 200:
        message = f"A pipeline named {name} in project {project} exists."
        log.debug(message)
        import_type = "update"

    elif status_code == 404:
        message = f"No pipeline named {name} was found in project {project}"
        log.debug(message)
        import_type = "create"

    else:
        message = f"Failed to determine whether the pipeline named {name} exists in project {project}"
        log.error(message)
        import_type = "error"

    # When the pipeline does not exist, import it.
    if import_type == "create":
        log.debug("Importing new pipeline")

        try:
            (
                response_yaml,
                status_code,
            ) = pipeline.import_pipeline(
                settings=settings,
                bearer_token=bearer_token,
                pipeline_spec=pipeline_spec,
            )

        except Exception as err:
            message = f"An exception occurred while importing pipeline {name}."
            log.error(message)
            log.error(err)
            return 1

        if config.TRACE_ENABLED:
            log.debug(response_yaml)

    # When the pipeline already exists, update it.
    elif import_type == "update":
        log.debug("Updating existing pipeline")

        try:
            (
                response_yaml,
                status_code,
            ) = pipeline.update_pipeline(
                settings=settings,
                bearer_token=bearer_token,
                pipeline_spec=pipeline_spec,
            )

        except Exception as err:
            message = f"An exception occurred while updating pipeline {name}."
            log.error(message)
            log.error(err)
            return 1

        if config.TRACE_ENABLED:
            log.debug(response_yaml)

    # When dry run is enabled, show a message.
    elif import_type == "disabled":
        log.info("Dry run enabled, skipping pipeline import.")
        status_code = 200

    else:
        log.error("Unknown pipeline import type %s", import_type)
        status_code = 000

    result = rest.check_status_code(status_code)
    return result
