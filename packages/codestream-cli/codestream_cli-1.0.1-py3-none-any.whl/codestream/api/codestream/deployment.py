#!/usr/bin/env python3

"""
Deployment module.

A collection of functions for working with
vRA Code Stream pipelines deployments.
"""

import logging

import json
import requests

from codestream.common import config, logger, whoami

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------


def get_id(settings, bearer_token, name, project):
    """
    Lookup deployment IDs.

    Lookup deployment IDs for a given pipeline name and project.

    Inputs:

    - vRA URL
    - vRA Access Token
    - Pipeline Name
    - Pipeline Project

    Output:

    - Result message
    - Status Code
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    """
    #encodedName = parse.quote(name)
    #uri="/deployment/api/deployments?name={0}&apiVersion=2022-06-27&expand=resources"
    #authorisation = "Bearer " + get_bearer_token()
    #header = {"Content-Type": "application/json",
    #          "Authorization": authorisation, "Accept": "application/json"}
    #fullUrl = vra_url + uri.format(encodedName)
    #try:
    #    result = requests.get(fullUrl, headers=header, verify=False)
    #except requests.exceptions.RequestException as e:
    #    print(f"Response: {json.dumps(response)}")
    #    raise SystemExit(e)
    #else:
    #    jsonResponse = result.json()
    ## Just return the 1st match
    #if jsonResponse["content"] and len(jsonResponse["content"]) > 0:
    #    return jsonResponse["content"][0]["id"]
    #else:
    #    return ''
    #
    """

    # TODO: FINISH THIS
    deployment_id = "12345"
    status_code = 200
    return deployment_id, status_code


def delete_id(settings, bearer_token, id):
    """
    Delete a deployment by ID.

    Delete a pipeline deployment by providing the ID.

    Inputs:

    - vRA URL
    - vRA Access Token
    - Deployment ID

    Output:

    - Result message
    - Status Code
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # Build the final URL that will be used.
    uri = "/deployment/api/deployments/"
    full_url = settings.url + uri + id

    # Build request body and header
    authorisation = "Bearer" + bearer_token
    header = {
        "Content-Type": "application/json",
        "Authorization": authorisation,
        "Accept": "application/json",
    }

    # Are we validating certs?
    if settings.insecure:
        verify = False
    else:
        verify = True

    if settings.dry_run:
        text = f"URL: {full_url} " f"INSECURE: {verify} " f"HEADERS: {header} "
        logger.eprint(text)
        response_json = {}
        status_code = 200

    try:
        response = requests.delete(full_url, headers=header, verify=verify)

        response_json = response.json()
        status_code = response.status_code

    except Exception as err:
        log.exception(err)
        raise

    log.debug("Debug info")
    log.debug(json.dumps(response_json, indent=4))
    log.debug(status_code)

    return status_code
