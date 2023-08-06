#!/usr/bin/env python3

"""
Pipelines.

Argument handling for the 'pipelines' subcommand.
"""

import logging
import textwrap

from codestream.api.auth import get_bearer_token
from codestream.cli.args import CONSOLE_PARSER
from codestream.cli.subcommands import subcommand, argument
from codestream.common import (
    config,
    logger,
    rest,
    validate_url,
    VRASettings,
    whoami,
)
from codestream.cli.subcommands.pipelines import (
    check,
    delete,
    enable,
    execute,
    exports,
    get,
    imports,
    validate,
)  # noqa: F401

__all__ = [
    "check",
    "delete",
    "enable",
    "execute",
    "exports",
    "get",
    "imports",
    "validate",
]

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Subcommand: Pipeline
# ---------------------------------------------------------------------------


@subcommand(
    [
        argument(
            "-cp",
            "--check-pipeline",
            help=textwrap.dedent(
                """\

                Check if a pipeline exists by providing a name and project.

                Requires the following arguments passed globally.

                --url          The vRA URL. Defaults to $CODESTREAM_CLI_VRA_URL
                --token        The token to authenticate with.

                Requires the following arguments passed to the subcommand.

                --name         The pipeline name
                --project      The pipeline project

            """
            ),
            action="store_true",
        ),
        argument(
            "-dp",
            "--delete-pipeline",
            help=textwrap.dedent(
                """\

                Delete a Code Stream pipeline.

                Requires the following arguments passed globally.

                --url          The vRA URL. Defaults to $CODESTREAM_CLI_VRA_URL
                --token        The token to authenticate with.

                Requires the following arguments passed to the subcommand.

                --name         The pipeline name
                --project      The pipeline project

            """
            ),
            action="store_true",
        ),
        argument(
            "-ep",
            "--enable-pipeline",
            help=textwrap.dedent(
                """\

                Enable a Code Stream pipeline.

                Requires the following arguments passed globally.

                --url          The vRA URL. Defaults to $CODESTREAM_CLI_VRA_URL
                --token        The token to authenticate with.

                Requires the following arguments passed to the subcommand.

                --name         The pipeline name
                --project      The pipeline project

            """
            ),
            action="store_true",
        ),
        argument(
            "-exp",
            "--execute-pipeline",
            help=textwrap.dedent(
                """\

                Execute a Code Stream pipeline.

                Requires the following arguments passed globally.

                --url          The vRA URL. Defaults to $CODESTREAM_CLI_VRA_URL
                --token        The token to authenticate with.

                Requires the following arguments passed to the subcommand.

                --name         The pipeline name
                --project      The pipeline project

                Optional arguments can be passed to the subcommand.

                --inputs       Additional Pipeline inputs.

            """
            ),
            action="store_true",
        ),
        argument(
            "-xp",
            "--export-pipeline",
            help=textwrap.dedent(
                """\

                Export a Code Stream pipeline.

                Requires the following arguments passed globally.

                --url          The vRA URL. Defaults to $CODESTREAM_CLI_VRA_URL
                --token        The token to authenticate with.

                Requires the following arguments passed to the subcommand.

                --name         The pipeline name
                --project      The pipeline project

                Optional arguments can be passed to the subcommand.

                --file         Write the output to file instead of on-screen.

            """
            ),
            action="store_true",
        ),
        argument(
            "-gpex",
            "--get-pipeline-executions",
            help=textwrap.dedent(
                """\

                Get pipeline executions by providing a name and project.

                Requires the following arguments passed globally.

                --url          The vRA URL. Defaults to $CODESTREAM_CLI_VRA_URL
                --token        The token to authenticate with.

                Requires the following arguments passed to the subcommand.

                --name         The pipeline name
                --project      The pipeline project

            """
            ),
            action="store_true",
        ),
        argument(
            "-gpid",
            "--get-pipeline-id",
            help=textwrap.dedent(
                """\

                Get a pipeline ID by providing a name and project.

                Requires the following arguments passed globally.

                --url          The vRA URL. Defaults to $CODESTREAM_CLI_VRA_URL
                --token        The token to authenticate with.

                Requires the following arguments passed to the subcommand.

                --name         The pipeline name
                --project      The pipeline project

            """
            ),
            action="store_true",
        ),
        argument(
            "-gp",
            "--get-pipeline-info",
            help=textwrap.dedent(
                """\

                Get info about a pipeline by providing a name and project.

                Requires the following arguments passed globally.

                --url          The vRA URL. Defaults to $CODESTREAM_CLI_VRA_URL
                --token        The token to authenticate with.

                Requires the following arguments passed to the subcommand.

                --name         The pipeline name
                --project      The pipeline project

            """
            ),
            action="store_true",
        ),
        argument(
            "-ip",
            "--import-pipeline",
            help=textwrap.dedent(
                """\

                Import a Code Stream pipeline from a file.

                If a pipeline with the same name & project does not exist,
                it is imported.

                If the pipeline with the same name & project already exists,
                it is updated.

                Requires the following arguments passed globally.

                --url          The vRA URL. Defaults to $CODESTREAM_CLI_VRA_URL
                --token        The token to authenticate with.

                Requires the following arguments passed to the subcommand.

                --file         The filename

            """
            ),
            action="store_true",
        ),
        argument(
            "-vp",
            "--validate-pipeline",
            help=textwrap.dedent(
                """\

                Validate a Code Stream pipeline YAML file meets the schema.

                Requires the following arguments passed globally.

                None

                Requires the following arguments passed to the subcommand.

                --file         The filename

            """
            ),
            action="store_true",
        ),
        argument(
            "-f",
            "--file",
            help=textwrap.dedent(
                """\

                The file name of the Code Stream pipeline.

                The file provided is expected to be valid YAML.

            """
            ),
            action="store",
        ),
        argument(
            "-i",
            "--inputs",
            help=textwrap.dedent(
                """\

                Additional pipeline variables provided as a JSON string.

            """
            ),
            action="store",
        ),
        argument(
            "-n",
            "--name",
            help=textwrap.dedent(
                """\

                The Code Stream pipeline name.

                The name can contain spaces by passing a quoted string.

            """
            ),
            action="store",
        ),
        argument(
            "-p",
            "--project",
            help=textwrap.dedent(
                """\

                The Code Stream pipeline project.

                The name can contain spaces by passing a quoted string.

            """
            ),
            action="store",
        ),
    ]
)
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
# pylint: disable=too-many-return-statements
def pipelines(args=None):  # noqa: C901
    """
    Code Stream pipelines.

    Subcommand for working with vRA Code Stream pipelines.

    Only one subcommand will be processed per execution.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)
        log.debug(args)

    ####################
    # Settings
    ####################

    # No point going anywhere without a valid URL.
    if not validate_url(args.url):
        CONSOLE_PARSER.print_help()
        message = (
            "Please provide a valid and DNS resolvable API URL "
            "either with --url or $CODESTREAM_CLI_VRA_URL. "
            f"{args.url} is invalid."
        )
        log.error(message)
        logger.eprint(message)
        return 1

    # Obtain vRA settings by merging defaults with user overrides.
    settings = VRASettings(
        dry_run=args.dry_run,
        url=args.url,
        insecure=args.insecure,
        timeout=args.timeout,
    )

    ####################
    # Validate Pipeline
    ####################

    if args.validate_pipeline:
        if config.TRACE_ENABLED:
            message = f"""
                Processing {args.subcommand} option --validate-pipeline
            """
            log.debug(message)

        result = validate.run(
            file=args.file,
        )

        if result:
            message = f"""
                The pipeline file {args.file} validated successfully.
            """
            log.info(message)
            print(message)
            return_code = 0

        else:
            message = f"""
                The pipeline file {args.file} failed validation.
            """
            log.error(message)
            logger.eprint(message)
            return_code = 1

        return return_code

    ####################
    # Access Token
    #
    # NOTE: All options from this point below, require a bearer token.
    ####################

    # All the commands require a token to be provided.
    if args.token is None or len(args.token) < 1:
        CONSOLE_PARSER.print_help()
        message = (
            "Please provide a valid Refresh Token with "
            "--token or $CODESTREAM_CLI_VRA_TOKEN."
        )
        log.error(message)
        logger.eprint(message)
        return 1

    # By convention, the bash scripts default to
    #  ${CODESTREAM_CLI_VRA_TOKEN:-EMPTY} to catch empty vars.
    if args.token == "EMPTY":
        message = (
            "The provided token was set to the string 'EMPTY'. "
            "Check the variable that was passed contains a valid token."
        )
        log.error(message)
        logger.eprint(message)
        return 1

    log.debug("A Refresh Token has been provided.")

    try:
        # Obtain an access token by using the provided refresh token.
        bearer_token, status_code = get_bearer_token(
            settings=settings,
            refresh_token=args.token,
        )

    # pylint: disable=broad-except
    except Exception as err:
        message = (
            "An exception occurred whilst obtaining an access token. "
            "Enable the debug log level for further information."
        )
        log.error(message)
        log.error(err)
        return 1

    # Ensure the access token was obtain successfully.
    result = rest.check_status_code(status_code)

    if result:
        message = "Successfully obtained bearer token"
        log.info(message)

    else:
        message = "Failed to obtain bearer token"
        log.error(message)
        logger.eprint(message)
        return 1

    ####################
    # Check Pipeline
    ####################

    if args.check_pipeline:
        if config.TRACE_ENABLED:
            message = f"Processing {args.subcommand} option --check-pipeline"
            log.debug(message)

        result = check.run(
            bearer_token=bearer_token,
            name=args.name,
            project=args.project,
            settings=settings,
        )

        if result:
            message = f"""
                A pipeline named {args.name}
                in the project {args.project} already exists
            """
            log.info(message)
            print(message)
            return_code = 0

        else:
            message = f"""
                A pipeline named {args.name}
                in the project {args.project} does not exist
            """
            log.error(message)
            logger.eprint(message)
            return_code = 1

        return return_code

    ####################
    # Delete Pipeline
    ####################

    if args.delete_pipeline:
        if config.TRACE_ENABLED:
            message = f"""
                Processing {args.subcommand} option --delete-pipeline
            """
            log.debug(message)

        result = delete.run(
            bearer_token=bearer_token,
            name=args.name,
            project=args.project,
            settings=settings,
        )

        if result:
            message = (
                f"The pipeline named {args.name} "
                f"in the project {args.project} "
                "was deleted successfully."
            )
            log.info(message)
            print(message)
            return_code = 0

        else:
            message = (
                "The pipeline named {args.name} "
                f"in the project {args.project} "
                "failed to be deleted."
            )
            log.error(message)
            logger.eprint(message)
            return_code = 1

        return return_code

    ####################
    # Enable Pipeline
    ####################

    if args.enable_pipeline:
        if config.TRACE_ENABLED:
            message = (
                f"Processing {args.subcommand} " "option --enable-pipeline"
            )
            log.debug(message)

        result = enable.run(
            bearer_token=bearer_token,
            name=args.name,
            project=args.project,
            settings=settings,
        )

        if result:
            message = (
                f"The pipeline named {args.name} "
                f"in the project {args.project} "
                "was enabled successfully."
            )
            log.info(message)
            print(message)
            return_code = 0

        else:
            message = (
                f"The pipeline named {args.name} "
                f"in the project {args.project} "
                "failed to be enabled."
            )
            log.error(message)
            logger.eprint(message)
            return_code = 1

        return return_code

    ####################
    # Execute Pipeline
    ####################

    if args.execute_pipeline:
        if config.TRACE_ENABLED:
            message = f"Processing {args.subcommand} option --execute-pipeline"
            log.debug(message)

        result = execute.run(
            bearer_token=bearer_token,
            name=args.name,
            project=args.project,
            inputs=args.inputs,
            settings=settings,
        )

        if result:
            message = (
                f"The pipeline named {args.name} "
                "in the project {args.project} "
                "was executed successfully."
            )
            log.info(message)
            print(message)
            return_code = 0

        else:
            message = (
                f"The pipeline named {args.name} "
                "in the project {args.project} "
                "failed to be executed."
            )
            log.error(message)
            logger.eprint(message)
            return_code = 1

        return return_code

    ####################
    # Export Pipeline
    ####################

    if args.export_pipeline:
        if config.TRACE_ENABLED:
            message = (
                f"Processing {args.subcommand} " "option --export-pipeline"
            )
            log.debug(message)

        result = exports.run(
            bearer_token=bearer_token,
            name=args.name,
            project=args.project,
            file=args.file,
            settings=settings,
        )

        if result:
            message = f"""
                The pipeline named {args.name}
                in the project {args.project}
                was exported successfully.
            """
            log.info(message)
            print(message)
            return_code = 0

        else:
            message = f"""
                The pipeline named {args.name}
                in the project {args.project}
                failed to be exported.
            """
            log.error(message)
            logger.eprint(message)
            return_code = 1

        return return_code

    ####################
    # Get Pipeline Info
    ####################

    if args.get_pipeline_info:
        if config.TRACE_ENABLED:
            message = f"""
                Processing {args.subcommand} option --get-pipeline
            """
            log.debug(message)

        result = get.run(
            bearer_token=bearer_token,
            name=args.name,
            project=args.project,
            info_type="all",
            settings=settings,
        )

        if result:
            message = f"""
                Successfully obtained info for pipeline named {args.name}
                in the project {args.project}
            """
            log.info(message)
            # The captured info is printed directly from the function,
            # send this to stderr instead.
            logger.eprint(message)
            return_code = 0

        else:
            message = f"""
                Failed to obtain info for pipeline named {args.name}
                in the project {args.project}
            """
            log.error(message)
            logger.eprint(message)
            return_code = 1

        return return_code

    ####################
    # Get Pipeline ID
    ####################

    if args.get_pipeline_id:
        if config.TRACE_ENABLED:
            message = f"""
                Processing {args.subcommand} option --get-pipeline-id
            """
            log.debug(message)

        result = get.run(
            bearer_token=bearer_token,
            name=args.name,
            project=args.project,
            info_type="id",
            settings=settings,
        )

        if result:
            message = f"""
                Successfully obtained ID for pipeline named {args.name}
                in the project {args.project}
            """
            log.info(message)
            # The captured info is printed directly from the function,
            # send this to stderr instead.
            logger.eprint(message)
            return_code = 0

        else:
            message = f"""
                Failed to obtain ID for pipeline named {args.name}
                in the project {args.project}
            """
            log.error(message)
            logger.eprint(message)
            return_code = 1

        return return_code

    ####################
    # Get Pipeline Executions
    ####################

    if args.get_pipeline_executions:
        if config.TRACE_ENABLED:
            message = f"""
                Processing {args.subcommand} option --get-pipeline-executions
            """
            log.debug(message)

        result = get.run(
            bearer_token=bearer_token,
            name=args.name,
            project=args.project,
            info_type="executions",
            settings=settings,
        )

        if result:
            message = f"""
                Successfully queried executions for pipeline named {args.name}
                in the project {args.project}
            """
            log.info(message)
            # The captured info is printed directly from the function,
            # send this to stderr instead.
            logger.eprint(message)
            return_code = 0

        else:
            message = (
                f"Failed to query executions for pipeline named {args.name} "
                "in the project {args.project} or there aren't any."
            )
            log.error(message)
            logger.eprint(message)
            return_code = 1

        return return_code

    ####################
    # Import Pipeline
    ####################

    if args.import_pipeline:
        if config.TRACE_ENABLED:
            message = f"""
                Processing {args.subcommand} option --import-pipeline
            """
            log.debug(message)

        result = imports.run(
            bearer_token=bearer_token,
            file=args.file,
            settings=settings,
        )

        if result:
            message = f"""
                Successfully imported pipeline from file {args.file}
            """
            log.info(message)
            print(message)
            return_code = 0

        else:
            message = f"""
                Failed to import pipeline from file {args.file}
            """
            log.error(message)
            logger.eprint(message)
            return_code = 1

        return return_code

    ####################
    # Fall through
    ####################

    CONSOLE_PARSER.print_help()
    logger.eprint(
        "Invalid or missing command."
        f"Try running 'codestream-cli {args.subcommand} --help' for more info."
    )
    return 1
