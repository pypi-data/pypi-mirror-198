#!/usr/bin/env python3

"""
Deployments.

Argument handling for the 'deployments' subcommand.
"""

import logging
import textwrap

from codestream.cli.args import CONSOLE_PARSER
from codestream.common import (
    config,
    logger,
    rest,
    validate_url,
    VRASettings,
    whoami,
)
from codestream.cli.subcommands import subcommand, argument

from codestream.api.auth import get_bearer_token
from codestream.api.codestream import deployment

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Subcommand: Deployment
# ---------------------------------------------------------------------------


@subcommand(
    [
        argument(
            "-gd",
            "--get-deployment",
            help=textwrap.dedent(
                """\

                Get a list of deployment Identifiers for a pipeline.

                Requires the following arguments passed globally.

                --token             The token to authenticate with.

                Requires the following arguments passed to the subcommand.

                --name              The pipeline name
                --project           The pipeline project

            """
            ),
            action="store_true",
        ),
        argument(
            "-deld",
            "--delete-deployment",
            help=textwrap.dedent(
                """\

                Delete a Code Stream deployment by providing the Identifier

                Requires the following arguments passed globally.

                --token             The token to authenticate with.

                Requires the following arguments passed to the subcommand.

                --id                The deployment identifier

            """
            ),
            action="store_true",
        ),
        argument(
            "-i",
            "--id",
            help=textwrap.dedent(
                """\

                The Code Stream deployment unique identifier.

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

            """
            ),
            action="store",
        ),
    ]
)
def deployments(args=None):
    """
    Code Stream deployments.

    Subcommand for working with vRA Code Stream deployments
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

    settings = VRASettings(
        dry_run=args.dry_run,
        url=args.url,
        insecure=args.insecure,
        timeout=args.timeout,
    )

    ####################
    # Access Token
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
    # ${CODESTREAM_CLI_VRA_TOKEN:-EMPTY} to catch empty vars.
    elif args.token == "EMPTY":
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

    if result != 0:
        log.error("Failed to obtain access token, unable to continue!")
        return 1

    ####################
    # Name
    ####################

    if args.name is None:
        CONSOLE_PARSER.print_help()
        log.error("You forgot to provide a pipeline name!")
        return 1

    ####################
    # Get Deployment
    ####################

    if args.get_deployment:
        if config.TRACE_ENABLED:
            log.debug("Processing %s option --get-deployment", args.subcommand)

        try:
            deployment_ids, status_code = deployment.get_id(
                settings=settings,
                bearer_token=bearer_token,
                name=args.name,
                project=args.project,
            )

        except Exception as err:
            message = (
                "An exception occurred whilst getting deployment {args.name}. "
                "Enable the debug log level for further information."
            )
            log.error(message)
            log.error(err)
            return 1

        log.info("Displaying deployment IDs for pipeline %s", args.name)
        logger.eprint(deployment_ids)

        result = rest.check_status_code(status_code)
        return result

    ####################
    # Delete Deployment
    ####################

    if args.delete_deployment:
        if config.TRACE_ENABLED:
            message = (
                f"Processing {args.subcommand} option " "--delete-deployment"
            )
            log.debug(message)
        try:
            status_code = deployment.delete_id(
                settings=settings,
                bearer_token=bearer_token,
                id=args.id,
            )

        except Exception as err:
            message = (
                "An exception occurred whilst "
                f"deleting deployment {args.name}. "
                "Enable the debug log level for further information."
            )
            log.error(message)
            log.error(err)
            return 1

        result = rest.check_status_code(status_code)
        return result

    ####################
    # Fall through
    ####################

    CONSOLE_PARSER.print_help()
    logger.eprint(
        "Invalid or missing command."
        f"Try running 'codestream-cli {args.subcommand} --help' for more info."
    )
    return 1
