#!/usr/bin/env python3

"""
Pipeline module.

A collection of functions for working with vRA Code Stream pipelines.
"""

import logging
import os
import pkgutil

import json
import jsonschema
import requests
import yaml

from codestream.common import config, logger, rest, VRASettings, whoami
from codestream.api.codestream import deployment

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------


def check_pipeline(
    bearer_token,
    name,
    project,
    settings=VRASettings,
):
    """
    Check Pipeline.

    Checks if a vRA Code Stream Pipeline exists by name.

    Inputs:

    - vRA URL
    - vRA Access Token
    - Pipeline Name
    - Pipeline Project

    Outputs:

    - Output message
    - Status Code

    API reference: ${VRA_URL}/pipeline/api/swagger/swagger-ui.html#/Pipelines/getPipelineByNameUsingGET
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # Build the full URL that will be used.
    api_version = "2019-10-17"
    encoded_name = requests.utils.quote(name)
    encoded_project = requests.utils.quote(project)
    uri = "/codestream/api/pipelines/{project}/{pipeline}?apiVersion={apiVersion}"
    formatted_url = uri.format(
        project=encoded_project, pipeline=encoded_name, apiVersion=api_version
    )
    full_url = settings.url + formatted_url

    # Build the request body and header.
    authorisation = "Bearer " + bearer_token
    header = {
        "Authorization": authorisation,
        "Accept": "*/*",
    }

    response_json, status_code = rest.call_vra_api(
        request_type="GET",
        response_type="json",
        content_type="json",
        settings=settings,
        full_url=full_url,
        header=header,
        body=None,
    )

    return response_json, status_code


def delete_pipeline(
    bearer_token,
    name,
    project,
    delete_deployment=False,
    settings=VRASettings,
):
    """
    Delete Pipeline.

    Delete a pipeline by name and project.

    Inputs:

    - vRA URL
    - vRA Access Token
    - Pipeline Name
    - Pipeline Project

    Outputs:

    - Output message
    - Status Code

    API reference: ${VRA_URL}/pipeline/api/swagger/swagger-ui.html#/Pipelines/deletePipelineByNameUsingDELETE
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # Are we deleting the deployment or just the pipeline?
    if delete_deployment:
        log.warning(
            "The deployment for pipeline {name} in project {project} is now being deleted."
        )

        # Obtain the deployment id.
        try:
            deployment_id, status_code = deployment.get_id(
                bearer_token=bearer_token,
                name=name,
                project=project,
                settings=settings,
            )

        except Exception as err:
            message = f"An exception occurred while obtaining deployment id for pipeline {name}."
            log.error(message)
            log.error(err)
            logger.eprint(err)
            return 1

        if config.TRACE_ENABLED:
            message = f"Deployment ID: {deployment_id}"
            log.debug(message)

        if status_code != 200:
            message = f"Error occurred while obtaining deployment id for pipeline {name}."
            log.error(message)
            logger.eprint(message)
            # Non-breaking error, continue anyway.

        else:
            # Delete the deployment.
            try:
                status_code = deployment.delete_id(
                    bearer_token=bearer_token,
                    deployment_id=deployment_id,
                    settings=settings,
                )

            except Exception as err:
                message = f"An exception occurred while deleting deployment id {deployment_id} for pipeline {name}."
                log.error(message)
                log.error(err)
                logger.eprint(err)
                return 1

            if status_code == 200:
                message = f"Deployment id {deployment_id} for pipeline {name} in project {project} was successfully deleted."
                log.info(message)
                logger.eprint(message)
            else:
                message = f"Deployment id {deployment_id} for pipeline {name} in project {project} failed to be deleted."
                log.error(message)
                logger.eprint(message)
                # Non-breaking error, continue anyway.

    else:
        log.info(
            "The deployment for pipeline {name} in project {project} will not be deleted."
        )

    # Build the full URL that will be used.
    api_version = "2019-10-17"
    encoded_name = requests.utils.quote(name)
    encoded_project = requests.utils.quote(project)
    uri = "/codestream/api/pipelines/{project}/{pipeline}?apiVersion={apiVersion}"
    formatted_url = uri.format(
        project=encoded_project, pipeline=encoded_name, apiVersion=api_version
    )
    full_url = settings.url + formatted_url

    # Build the request body and header.
    authorisation = "Bearer " + bearer_token
    header = {
        "Authorization": authorisation,
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    response_json, status_code = rest.call_vra_api(
        request_type="DELETE",
        response_type="json",
        content_type="json",
        settings=settings,
        full_url=full_url,
        header=header,
        body=None,
    )

    return response_json, status_code


def enable_pipeline(
    bearer_token,
    name,
    project,
    settings=VRASettings,
):
    """
    Enable Pipeline.

    Enables a vRA Code Stream Pipeline by name and project.

    Inputs:

    - vRA URL
    - vRA Access Token
    - Pipeline Name
    - Pipeline Project

    Outputs:

    - Output message
    - Status Code

    API reference: ${VRA_URL}/
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # Build the full URL that will be used.
    api_version = "2019-10-17"
    encoded_name = requests.utils.quote(name)
    encoded_project = requests.utils.quote(project)
    uri = "/codestream/api/pipelines/{project}/{pipeline}?apiVersion={apiVersion}"
    formatted_url = uri.format(
        project=encoded_project, pipeline=encoded_name, apiVersion=api_version
    )
    full_url = settings.url + formatted_url

    # Build the request body and header.
    authorisation = "Bearer " + bearer_token
    header = {
        "Authorization": authorisation,
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    body = {"enabled": "true"}

    response_json, status_code = rest.call_vra_api(
        request_type="PATCH",
        response_type="json",
        content_type="json",
        settings=settings,
        full_url=full_url,
        header=header,
        body=body,
    )

    return response_json, status_code


def execute_pipeline(
    bearer_token,
    name,
    project,
    inputs=None,
    settings=VRASettings,
):
    """
    Execute Pipeline.

    Executes a vRA Code Stream Pipeline by name and project.

    Inputs:

    - vRA URL
    - vRA Access Token
    - Pipeline Name
    - Pipeline Project
    - Optional input parameters

    Outputs:

    - Output message
    - Status Code

    API reference: ${VRA_URL}/pipeline/api/swagger/swagger-ui.html#/Pipelines/executePipelineByNameUsingPOST
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # Build the full URL that will be used.
    api_version = "2019-10-17"
    encoded_name = requests.utils.quote(name)
    encoded_project = requests.utils.quote(project)
    uri = "/codestream/api/pipelines/{project}/{pipeline}/executions?apiVersion={apiVersion}"
    formatted_url = uri.format(
        project=encoded_project, pipeline=encoded_name, apiVersion=api_version
    )
    full_url = settings.url + formatted_url

    # Are we providing extra inputs?
    if inputs:
        log.debug("Passing provided inputs to pipeline execution")
        pipeline_inputs = json.loads(inputs)

    else:
        log.debug("No additional inputs provided to pipeline execution")
        pipeline_inputs = {}

    if config.TRACE_ENABLED:
        log.debug(json.dumps(pipeline_inputs))

    # Build the request body and header.
    authorisation = "Bearer " + bearer_token
    header = {
        "Authorization": authorisation,
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    body = {
        "comments": "Executed by codestream-cli.",
        "input": pipeline_inputs,
    }

    response_json, status_code = rest.call_vra_api(
        request_type="POST",
        response_type="json",
        content_type="json",
        settings=settings,
        full_url=full_url,
        header=header,
        body=body,
    )

    # A status_code of '202' means the execution was "accepted" and running asynchronously.
    if status_code == 202:
        message = f"Re-mapping status code {status_code} to 200"
        log.debug(message)
        status_code = 200

    return response_json, status_code


def export_pipeline(
    bearer_token,
    name,
    project,
    settings=VRASettings,
):
    """
    Export a Code Stream Pipeline.

    Exports a Code Stream Pipeline to a file path in YAML format.

    It is not the job of this function to determine if the pipeline already exists.

    Inputs:

    - vRA URL
    - vRA Access Token
    - Pipeline Name
    - Pipeline Project
    - File path

    Outputs:

    - File contents
    - Status Message
    - Return Code

    API reference: ${VRA_URL}/pipeline/api/swagger/swagger-ui.html#/Pipelines/exportUsingGET
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # Build the full URL that will be used.
    api_version = "2019-10-17"
    encoded_name = requests.utils.quote(name)
    encoded_project = requests.utils.quote(project)
    uri = "/codestream/api/export?pipelines={pipeline}&project={project}&apiVersion={apiVersion}"
    formatted_url = uri.format(
        project=encoded_project, pipeline=encoded_name, apiVersion=api_version
    )
    full_url = settings.url + formatted_url

    # Build the request body and header.
    authorisation = "Bearer " + bearer_token
    header = {
        "Authorization": authorisation,
        "Accept": "application/x-yaml",  # The API returns a YAML object.
    }

    response_yaml, status_code = rest.call_vra_api(
        request_type="GET",
        response_type="text",
        content_type="json",
        settings=settings,
        full_url=full_url,
        header=header,
        body=None,
    )

    return response_yaml, status_code


def get_pipeline(
    bearer_token,
    name,
    project,
    settings=VRASettings,
):
    """
    Get Code Stream Pipeline information based on provided filter.

    By default returns all fields unless return_id_only=True

    Inputs:

    - vRA URL
    - vRA Access Token
    - Pipeline Name
    - Pipeline Project

    Outputs:

    - Pipeline info or ID
    - Status Code

    API reference: ${VRA_URL}/pipeline/api/swagger/swagger-ui.html#/Pipelines/getAllPipelinesUsingGET
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # Build the full URL that will be used.
    api_version = "2019-10-17"
    encoded_name = requests.utils.quote(name)
    encoded_project = requests.utils.quote(project)
    encoded_filter_name = requests.utils.quote("name eq ")
    encoded_filter_project = requests.utils.quote("project eq ")
    uri = "/codestream/api/pipelines?$filter={filter_name}'{pipeline}'&$filter={filter_project}'{project}'&apiVersion={apiVersion}"
    formatted_url = uri.format(
        filter_name=encoded_filter_name,
        filter_project=encoded_filter_project,
        project=encoded_project,
        pipeline=encoded_name,
        apiVersion=api_version,
    )
    full_url = settings.url + formatted_url

    # Build the request body and header.
    authorisation = "Bearer " + bearer_token
    header = {
        "Authorization": authorisation,
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    response_json, status_code = rest.call_vra_api(
        request_type="GET",
        response_type="json",
        content_type="json",
        settings=settings,
        full_url=full_url,
        header=header,
        body=None,
    )

    return response_json, status_code


def get_pipeline_executions(
    bearer_token,
    name,
    project,
    settings=VRASettings,
):
    """
    Get Pipeline executions.

    Returns executions IDs for a provided pipeline name and project.

    Inputs:

    - vRA URL
    - vRA Access Token
    - Pipeline Name
    - Pipeline Project

    Outputs:

    - Pipeline execution IDs.
    - Status Code

    API reference: ${VRA_URL}/pipeline/api/swagger/swagger-ui.html#/Pipelines/getExecutionsByNameUsingGET
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # Build the full URL that will be used.
    api_version = "2019-10-17"
    uri = "/codestream/api/pipelines/{project}/{pipeline}/executions?apiVersion={apiVersion}"
    formatted_url = uri.format(
        pipeline=name,
        project=project,
        apiVersion=api_version,
    )
    full_url = settings.url + formatted_url

    # Build the request body and header.
    authorisation = "Bearer " + bearer_token
    header = {
        "Authorization": authorisation,
        "Accept": "*/*",
    }

    response_json, status_code = rest.call_vra_api(
        request_type="GET",
        response_type="json",
        content_type="json",
        settings=settings,
        full_url=full_url,
        header=header,
        body=None,
    )

    return response_json, status_code


def import_pipeline(
    bearer_token,
    pipeline_spec,
    settings=VRASettings,
):
    """
    Import a Code Stream Pipeline.

    Imports a Code Stream Pipeline from a file in YAML format.

    Note the API endpoint will not override or update an existing pipeline.

    It is not the job of this function to determine if the pipeline already exists.
    It is not the job of this function to determine if the provided YAML is valid.

    Inputs:

    - vRA URL
    - vRA Access Token
    - The YAML contents of a file.

    Outputs:

    - Status Message
    - Return Code

    API reference: ${VRA_URL}/pipeline/api/swagger/swagger-ui.html#/Pipelines/importYamlUsingPOST
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # Build the full URL that will be used.
    api_version = "2019-10-17"
    uri = "/codestream/api/import?apiVersion={apiVersion}"
    formatted_url = uri.format(apiVersion=api_version)
    full_url = settings.url + formatted_url

    # Double check that both the name and project are populated.
    if not pipeline_spec.get("name") or not pipeline_spec.get("project"):
        message = "Failed to extract the mandatory fields (name,project) from the provided pipeline spec"
        logger.eprint(message)
        log.error(message)
        return 1

    # Build the request body and header.
    authorisation = "Bearer " + bearer_token
    header = {
        "Authorization": authorisation,
        "Accept": "application/x-yaml",
        "Content-Type": "application/x-yaml",
    }
    body = pipeline_spec

    response_yaml, status_code = rest.call_vra_api(
        request_type="POST",
        response_type="text",
        content_type="text",
        settings=settings,
        full_url=full_url,
        header=header,
        body=body,
    )

    return response_yaml, status_code


def update_pipeline(
    bearer_token,
    pipeline_spec,
    settings=VRASettings,
):
    """
    Update a Code Stream Pipeline.

    Updates an existing Code Stream Pipeline from a file in YAML format.

    Note the API endpoint will not create a new pipeline if it doesn't exist.

    It is not the job of this function to determine if the provided YAML is valid.

    Inputs:

    - vRA URL
    - vRA Access Token
    - The YAML contents of a file.

    Outputs:

    - Status Message
    - Return Code

    API reference: ${VRA_URL}/pipeline/api/swagger/swagger-ui.html#/Pipelines/importYamlUsingPOST
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # Double check that both the name and project are populated.
    if not pipeline_spec.get("name") or not pipeline_spec.get("project"):
        message = "Failed to extract the mandatory fields (name,project) from the provided pipeline spec"
        logger.eprint(message)
        log.error(message)
        return 1

    # Extract the pipeline name and project from the YAML.
    name = pipeline_spec["name"]
    project = pipeline_spec["project"]

    # Build the full URL that will be used.
    api_version = "2019-10-17"
    uri = "/codestream/api/pipelines/{project}/{pipeline}?apiVersion={apiVersion}"
    formatted_url = uri.format(
        pipeline=name,
        project=project,
        apiVersion=api_version,
    )
    full_url = settings.url + formatted_url

    # Build the request body and header.
    authorisation = "Bearer " + bearer_token
    header = {
        "Authorization": authorisation,
        "Accept": "*/*",
        "Content-Type": "application/json",
    }
    body = pipeline_spec

    response_yaml, status_code = rest.call_vra_api(
        request_type="PUT",
        response_type="json",
        content_type="json",
        settings=settings,
        full_url=full_url,
        header=header,
        body=body,
    )

    return response_yaml, status_code


def validate_pipeline(pipeline_yaml):
    """
    Validate Code Stream YAML.

    Takes a YAML object of a Code Stream pipeline as input and returns the
    pipeline specification as a JSON object.

    This conformant object can then be used to pass to the vRA API.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # These were generated using openapi2jsonschema from the live vRA API.
    dir_schemas = "swagger/schemas/"
    # dir_examples = "swagger/examples/"

    # Read in the current schema file for Code Steam pipelines.
    file = dir_schemas + "pipelinespec.json"
    try:
        schema_file_contents = pkgutil.get_data(__name__, file)

    except OSError as err:
        log.error("Failed to open the schame file %s", file)
        log.error(err)
        raise OSError from err

    except Exception as err:
        log.error("Unhandled exception opening scheam file %s", file)
        log.error(err)
        raise Exception from err

    # Ensure the loaded schema is valid json.
    try:
        pipeline_schema = json.loads(schema_file_contents)
        pwd = os.path.dirname(os.path.realpath(__file__))

        resolver = jsonschema.RefResolver(
            referrer=pipeline_schema,
            base_uri="file://" + pwd + "/" + dir_schemas,
        )

    except Exception as err:
        log.error("Failed to load valid json fom file %s", file)
        log.error(err)
        raise Exception from err

    # Convert the current YAML pipeline provided into a JSON object
    pipeline_json = yaml.load(pipeline_yaml, Loader=yaml.SafeLoader)

    """
    # TEST: Test a mock example to ensure the function is valid.
    # TODO: Move this to a unit test.

    # Read in the current schema file for Code Steam pipelines.
    file2 = dir_examples + "pipelinespec.json"
    try:
        spec_file = open(os. path. join(os. path. dirname(__file__), file2), 'r')

    except OSError:
        print(f"Could not open file: {file2}")
        sys.exit(1)

    else:
        spec_file_contents = spec_file.read()

    # Ensure the loaded spec is valid json.
    try:
        pipeline_spec = json.loads(spec_file_contents)

    except Exception as err:
        print(f"Failed to load json valid json from file {file}")
        print(err)
        sys.exit(1)
    """

    # TODO: Work with the vRA Consultant
    #       - What are the minimum required fields?
    #       - What should we set as required for our configuration?
    #       - Set the fields in the 'required' set of the spec file.
    #       - Set minLength where possible to avoid empty strings.

    # Craft a specification using the existing objects or set defaults when empty.
    pipeline_spec = {}
    pipeline_spec["state"] = "RELEASED"
    pipeline_spec["kind"] = pipeline_json.get("kind", "")
    pipeline_spec["project"] = pipeline_json.get("project", "")
    pipeline_spec["name"] = pipeline_json.get("name", "")
    pipeline_spec["icon"] = pipeline_json.get("icon", "")
    pipeline_spec["enabled"] = pipeline_json.get("enabled", "")
    pipeline_spec["description"] = pipeline_json.get("description", "")
    pipeline_spec["concurrency"] = pipeline_json.get("concurrency", "")
    pipeline_spec["options"] = pipeline_json.get("options", [])
    pipeline_spec["input"] = pipeline_json.get("input", {})
    pipeline_spec["_inputMeta"] = pipeline_json.get("_inputMeta", {})
    pipeline_spec["workspace"] = pipeline_json.get("workspace", {})
    pipeline_spec["output"] = pipeline_json.get("output", {})
    pipeline_spec["stageOrder"] = pipeline_json.get("stageOrder", [])
    pipeline_spec["stages"] = pipeline_json.get("stages", {})
    pipeline_spec["rollbacks"] = pipeline_json.get("rollbacks", [])
    pipeline_spec["notifications"] = pipeline_json.get("notifications", {})
    pipeline_spec["starred"] = pipeline_json.get("starred", {})
    pipeline_spec["tags"] = pipeline_json.get("tags", [])

    if config.TRACE_ENABLED:
        log.debug("%s", json.dumps(pipeline_spec, indent=4))

    # Validate the crafted spec against the schema
    try:
        jsonschema.validate(
            instance=pipeline_spec, schema=pipeline_schema, resolver=resolver
        )

    except jsonschema.exceptions.ValidationError as err:
        log.error("Validation error! %s on path %s", err.message, err.path)
        log.debug("Path: %s", err.path)
        log.debug("Validator: %s", err.validator)
        log.debug("Context: %s", err.context)
        log.debug("Cause: %s", err.cause)
        log.debug("Schema: %s", err.schema)

        return pipeline_spec, False

    except jsonschema.exceptions.SchemaError as err:
        log.error("Schema error! %s", err.message)
        errors = sorted(err.iter_errors(pipeline_spec), key=lambda e: e.path)
        for error in errors:
            for suberror in sorted(error.context, key=lambda e: e.schema_path):
                log.error(
                    list(suberror.schema_path), suberror.message, sep=", "
                )
        return pipeline_spec, False

    except Exception as err:
        log.error("Unhandled exception while validating file against schema!")
        log.error(err)
        raise Exception from err

    return pipeline_spec, True
