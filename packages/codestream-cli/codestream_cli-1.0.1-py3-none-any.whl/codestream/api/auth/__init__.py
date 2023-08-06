#!/usr/bin/env python3

"""
Authentication module.

A collection of functions for working with vRA authentication.
"""

import logging

from codestream.common import config, rest, VRASettings, whoami

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------


def get_refresh_token(username, password, settings=VRASettings):
    """
    Get refresh token.

    Get a refresh token from a provided vRA URL using a username and password.

    This token is long-lived.

    Inputs:

    - vRA URL
    - Username
    - Password

    Outputs:

    - Refresh Token
    - Status Code

    API reference: ${VRA_URL}/identity/doc/v3/api-docs/swagger-config#/LoginController/login_1
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # Build the full URL that will be used.
    uri = "/csp/gateway/am/api/login?access_token"
    full_url = settings.url + uri

    # Build the request body and header.
    header = {
        "Content-Type": "application/json",
        "Accept": "*/*",
    }
    body = {"username": username, "password": password}

    response_json, status_code = rest.call_vra_api(
        request_type="POST",
        response_type="json",
        content_type="json",
        settings=settings,
        full_url=full_url,
        header=header,
        body=body,
    )

    if settings.dry_run:
        refresh_token = "DRY_RUN_ENABLED"
    elif not response_json.get("refresh_token"):
        refresh_token = "NO_TOKEN"  # nosec
    else:
        refresh_token = response_json["refresh_token"]

    return refresh_token, status_code


def get_bearer_token(refresh_token, settings=VRASettings):
    """
    Get bearer token.

    Get a bearer access token from a provided vRA URL by providing a refresh token.

    This token is short-lived.

    Inputs:

    - vRA URL
    - Refresh Token

    Outputs:

    - Bearer Token
    - Status Code

    API reference: ${VRA_URL}/iaas/api/swagger/ui/#/Login/retrieveAuthToken
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # Build the full URL that will be used.
    api_version = "2021-07-15"
    uri = "/iaas/api/login?apiVersion={api_version}"
    formatted_url = uri.format(api_version=api_version)
    full_url = settings.url + formatted_url

    # Build the request body and header
    header = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    body = {"refreshToken": refresh_token}

    response_json, status_code = rest.call_vra_api(
        request_type="POST",
        response_type="json",
        content_type="json",
        settings=settings,
        full_url=full_url,
        header=header,
        body=body,
    )

    if settings.dry_run:
        bearer_token = "DRY_RUN_ENABLED"
    elif not response_json.get("token"):
        bearer_token = "NO_TOKEN"  # nosec
    else:
        bearer_token = response_json["token"]

    return bearer_token, status_code
