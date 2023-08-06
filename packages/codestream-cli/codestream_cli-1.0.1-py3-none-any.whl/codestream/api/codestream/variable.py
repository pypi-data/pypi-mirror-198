#!/usr/bin/env python3

"""
Variables module.

A collection of functions for working with vRA Code Stream variables.
"""

import logging

from codestream.common import config, rest, VRASettings, whoami

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Classes
# ---------------------------------------------------------------------------


class VRAVariable:
    """
    Variable as a reusable class.

    Args:
        object (class): Reusable object holding vRA variable info.
    """

    def __init__(self, var_project, var_name, var_desc, var_type, var_value):
        """Fields for a variable in vRA."""
        self.project = var_project
        self.name = var_name
        self.description = var_desc
        self.type = var_type
        self.value = var_value


# ---------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------


def get(bearer_token, settings=VRASettings, variable=VRAVariable):
    """
    Get a variable.

    Args:
        settings (VRASettings): vRA Settings
        bearer_token (string): vRA Access Token
        variable (VRAVariable): vRA Variable fields.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # Build the full URL that will be used.
    api_version = "2019-10-17"
    uri = "/codestream/api/variables/{project}/{name}?apiVersion={api_version}"
    formatted_url = uri.format(
        project=variable.project, name=variable.name, api_version=api_version
    )
    full_url = settings.url + formatted_url

    # Build the request body and header.
    authorisation = "Bearer " + bearer_token
    header = {
        "Content-Type": "application/json",
        "Authorization": authorisation,
        "Accept": "application/json",
    }
    body = {
        "project": variable.project,
        "name": variable.name,
        "description": variable.description,
        "type": variable.type,
        "value": variable.value,
    }

    response_json, status_code = rest.call_vra_api(
        request_type="GET",
        response_type="json",
        content_type="json",
        settings=settings,
        full_url=full_url,
        header=header,
        body=body,
    )

    return response_json, status_code


def update(bearer_token, settings=VRASettings, variable=VRAVariable):
    """
    Update a variable.

    Args:
        settings (VRASettings): vRA Settings
        bearer_token (string): vRA Access Token
        variable (VRAVariable): vRA Variable fields.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # Build the full URL that will be used.
    api_version = "2019-10-17"
    uri = "/codestream/api/variables/{project}/{name}?apiVersion={api_version}"
    formatted_url = uri.format(
        project=variable.project, name=variable.name, api_version=api_version
    )
    full_url = settings.url + formatted_url

    # Build the request body and header.
    authorisation = "Bearer " + bearer_token
    header = {
        "Content-Type": "application/json",
        "Authorization": authorisation,
        "Accept": "application/json",
    }
    body = {
        "project": variable.project,
        "name": variable.name,
        "description": variable.description,
        "type": variable.type,
        "value": variable.value,
    }

    response_json, status_code = rest.call_vra_api(
        request_type="PUT",
        response_type="json",
        content_type="json",
        settings=settings,
        full_url=full_url,
        header=header,
        body=body,
    )

    return response_json, status_code
