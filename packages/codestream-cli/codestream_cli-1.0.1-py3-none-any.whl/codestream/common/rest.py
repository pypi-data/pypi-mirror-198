#!/usr/bin/env python3

"""
REST module.

Reusable functions for working with REST APIs.
"""

import logging

import json
import requests

from codestream.common import config, logger, VRASettings, whoami

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------


def check_status_code(status_code):
    """
    Check status_code.

    A generic catch all check for API status codes until specific checks can be created.

    Returns:
        bool: A boolean for success or failure based on status code.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # Need python > 3.10 for match. :(

    if status_code == 200:
        log.debug("%s OK", status_code)
        return True

    if status_code == 401:
        log.error("%s Unauthorized Request", status_code)
        return False

    if status_code == 403:
        log.error("%s Forbidden Request", status_code)
        return False

    if status_code == 404:
        log.error("%s Not Found", status_code)
        return False

    if status_code == 500:
        log.error("%s Server Side error", status_code)
        return False

    if status_code == 000:
        log.error(
            "A general error occurred. Review the log output or enable debug log level for further information."
        )
        return False

    log.error("%s Unhandled error status.", status_code)
    return False


def call_vra_api(
    full_url,
    request_type="GET",
    response_type="json",
    content_type="json",
    header="{}",
    body="{}",
    settings=VRASettings,
):
    """
    Call the vRA API.

    Raises:
        requests.exceptions.SSLError: _description_
        requests.exceptions.RequestException: _description_
        Exception: _description_

    Returns:
        integer: HTTP status code
        string: JSON response from API
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # Are we validating certificates?
    if settings.insecure:
        verify = False
    else:
        verify = True

    if content_type == "text":
        if body is None:
            data_str = str("{}")
        else:
            data_str = str(body)

    elif content_type == "json":
        if body is None:
            data_str = json.dumps("{}", indent=4)
            # data_json = json.loads("{}")
        else:
            data_str = json.dumps(body, indent=4)
            # data_json = json.loads(body)

    if settings.dry_run:
        text = (
            "DRY RUN ENABLED\n"
            f"URL: {full_url}\n"
            f"REQUEST: {request_type}\n"
            f"RESPONSE: {response_type}\n"
            f"CONTENT: {content_type}\n"
            f"VERIFY: {verify}\n"
            f"HEADER: {header}\n"
            f"BODY: {data_str}\n"
        )
        logger.eprint(text)

    else:
        try:
            # GET
            if request_type == "GET":
                response = requests.get(
                    full_url,
                    headers=header,
                    verify=verify,
                    data=data_str,
                    timeout=settings.timeout,
                )

            # POST
            if request_type == "POST":
                response = requests.post(
                    full_url,
                    headers=header,
                    verify=verify,
                    data=data_str,
                    timeout=settings.timeout,
                )

            # PUT
            if request_type == "PUT":
                response = requests.put(
                    full_url,
                    headers=header,
                    verify=verify,
                    data=data_str,
                    timeout=settings.timeout,
                )

            # DELETE
            if request_type == "DELETE":
                response = requests.delete(
                    full_url,
                    headers=header,
                    verify=verify,
                    data=data_str,
                    timeout=settings.timeout,
                )

            # PATCH
            if request_type == "PATCH":
                response = requests.patch(
                    full_url,
                    headers=header,
                    verify=verify,
                    data=data_str,
                    timeout=settings.timeout,
                )

        except requests.exceptions.SSLError as err:
            log.error(
                "SSL error during %s request type to %s",
                request_type,
                full_url,
            )
            log.error(err)
            raise requests.exceptions.SSLError from err

        except requests.exceptions.RequestException as err:
            log.error(
                "General exception during %s request type to %s",
                request_type,
                full_url,
            )
            log.error(err)
            raise requests.exceptions.RequestException from err

        except Exception as err:
            log.error(
                "Unhandled exception during %s request type to %s",
                request_type,
                full_url,
            )
            log.error(err)
            raise Exception from err

    try:
        if settings.dry_run:
            status_code = 200
        else:
            status_code = response.status_code

        if response_type == "text":
            if settings.dry_run:
                response_return = "DRY_RUN_ENABLED"
            else:
                response_return = response.text

        elif response_type == "json":
            if settings.dry_run:
                response_return = "{}"
            else:
                response_return = response.json()

        else:
            log.warning("Unspecified API response type, assuming JSON.")
            response_return = {}

    except Exception as err:
        log.error(
            "Unhandled exception processing %s request type to %s",
            request_type,
            full_url,
        )
        log.error(err)
        raise Exception from err

    if config.TRACE_ENABLED:
        log.debug("Debug info")
        log.debug(response_return)
        log.debug(status_code)

    return response_return, status_code
