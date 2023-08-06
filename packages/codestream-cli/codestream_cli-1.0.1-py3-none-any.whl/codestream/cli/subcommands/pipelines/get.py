#!/usr/bin/env python3

"""
Get Pipeline.

Argument handling for the 'pipelines' subcommand option '--get-pipeline'
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


def run(
    bearer_token=None,
    name=None,
    project=None,
    info_type="all",
    settings=VRASettings,
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

    if info_type == "all":
        result = _get_pipeline_info(
            bearer_token=bearer_token,
            name=name,
            project=project,
            settings=settings,
        )

    elif info_type == "executions":
        result = _get_pipeline_executions(
            bearer_token=bearer_token,
            name=name,
            project=project,
            settings=settings,
        )

    elif info_type == "id":
        result = _get_pipeline_ids(
            bearer_token=bearer_token,
            name=name,
            project=project,
            settings=settings,
        )

    else:
        message = f"Unknown info type {info_type} passed to function. Valid types are; 'all', 'id'"
        log.error(message)
        return False

    return result


def _get_pipeline_info(
    bearer_token=None, name=None, project=None, settings=VRASettings
):
    """
    Get pipeline info.

    Gets all available pipeline fields.

    Returns:
        result: Boolean True for success, False for failure.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    try:
        (
            response_json,
            status_code,
        ) = pipeline.get_pipeline(
            bearer_token=bearer_token,
            name=name,
            project=project,
            settings=settings,
        )

    except Exception as err:
        message = (
            f"An exception occurred whilst getting pipeline info for {name}."
        )
        log.error(message)
        log.error(err)
        return False

    if config.TRACE_ENABLED:
        log.debug(json.dumps(response_json, indent=4))

    result = rest.check_status_code(status_code)

    if result:
        message = f"Displaying pipeline results for query {name} in project {project}"
        log.info(message)

        # Print the response from the API to stdout.
        print(json.dumps(response_json, indent=4))

    return result


def _get_pipeline_executions(
    bearer_token=None, name=None, project=None, settings=VRASettings
):
    """
    Get pipeline executions.

    Gets all available pipeline execution ids.

    Returns:
        result: Boolean True for success, False for failure.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    try:
        (
            response_json,
            status_code,
        ) = pipeline.get_pipeline_executions(
            bearer_token=bearer_token,
            name=name,
            project=project,
            settings=settings,
        )

    except Exception as err:
        message = f"An exception occurred whilst getting pipeline executions for {name}."
        log.error(message)
        log.error(err)
        return False

    if config.TRACE_ENABLED:
        log.debug(json.dumps(response_json, indent=4))

    result = rest.check_status_code(status_code)

    if result:
        message = (
            f"Displaying execution IDs for filter {name} in project {project}"
        )
        log.info(message)

        # Extract the Pipeline executions from the response if present.
        if response_json["count"] is None:
            message = f"Unknown error checking executions for {name} in project {project}"
            log.error(message)
            logger.eprint(message)
            result = False
        elif response_json["count"] == 0:
            print(f"{name}: No executions found")
        else:
            count = response_json["count"]
            documents = response_json["documents"]

            message = (
                f"{count} executions found for {name} in project {project}"
            )
            log.info(message)
            logger.eprint(message)

            # Print the response from the API to stdout.
            loop = 0
            for document in documents:
                loop = loop + 1
                pipeline_name = documents[document]["name"]
                execution_id = documents[document]["id"]
                execution_status = documents[document]["status"]
                print(
                    f"{pipeline_name}: execution: {loop} {execution_id} status: {execution_status}"
                )

    return result


def _get_pipeline_ids(
    bearer_token=None, name=None, project=None, settings=VRASettings
):
    """
    Get pipeline ids.

    Gets pipeline identifiers based on provided query.

    Returns:
        result: Boolean True for success, False for failure.
    """
    try:
        (
            response_json,
            status_code,
        ) = pipeline.get_pipeline(
            bearer_token=bearer_token,
            name=name,
            project=project,
            settings=settings,
        )

    except Exception as err:
        message = f"An exception occurred whilst getting pipeline {name}."
        log.error(message)
        log.error(err)
        return False

    if config.TRACE_ENABLED:
        log.debug(json.dumps(response_json, indent=4))

    result = rest.check_status_code(status_code)

    if result:
        message = (
            f"Displaying pipeline IDs for filter {name} in project {project}"
        )
        log.info(message)

        # Extract the Pipeline Identifiers from the response if present.
        if response_json["count"] is None:
            message = (
                f"Unknown error checking IDs for {name} in project {project}"
            )
            log.error(message)
            logger.eprint(message)
            result = False
        elif response_json["count"] == 0:
            print(f"{name}: No IDs found")
        else:
            count = response_json["count"]
            documents = response_json["documents"]

            message = (
                f"{count} unique IDs found for {name} in project {project}"
            )
            log.info(message)
            logger.eprint(message)

        # Print the response from the API to stdout.
        for document in documents:
            pipeline_name = documents[document]["name"]
            pipeline_id = documents[document]["id"]
            print(f"{pipeline_name}: {pipeline_id}")

    return result
