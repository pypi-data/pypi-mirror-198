#!/usr/bin/env python3

"""
Variables.

Argument handling for the 'variables' subcommand.
"""

import logging
import textwrap

import json

from codestream.cli.args import CONSOLE_PARSER

# fmt: off
from codestream.common import (
    config,
    logger,
    rest,
    validate_url,
    VRASettings,
    whoami
)
# fmt: on
from codestream.cli.subcommands import subcommand, argument

from codestream.api.auth import get_bearer_token
from codestream.api.codestream import variable

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Subcommand: Variables
# ---------------------------------------------------------------------------


@subcommand(
    [
        argument(
            "-gv",
            "--get-variable",
            help=textwrap.dedent(
                """\
                Get a variable.

                Requires the following arguments passed globally.

                --token        The token to authenticate with.

                Requires the following arguments passed to the subcommand.

                --name         The variable name
                --project      The variable project

            """
            ),
            action="store_true",
        ),
        argument(
            "-sv",
            "--set-variable",
            help=textwrap.dedent(
                """\
                Update a variable.

                Requires the following arguments passed globally.

                --token        The token to authenticate with.

                Requires the following arguments passed to the subcommand.

                --name         The variable name
                --project      The variable project
                --value        The variable content
                --description  An optional variable description.

            """
            ),
            action="store_true",
        ),
        argument(
            "-p",
            "--project",
            help=textwrap.dedent(
                """\
                Project where the variable is located.

                Requires the following arguments passed globally.

                --token        The token to authenticate with.

                Requires the following arguments passed to the subcommand.

                --name         The variable name

            """
            ),
            action="store",
        ),
        argument(
            "-n",
            "--name",
            help=textwrap.dedent(
                """\
                Name of the variable.

                Requires the following arguments passed globally.

                --token        The token to authenticate with.

                Requires the following arguments passed to the subcommand.

                --project      The variable project

            """
            ),
            action="store",
        ),
        argument(
            "-d",
            "--description",
            help=textwrap.dedent(
                """\
                An optional description for the variable.

                Requires the following arguments passed globally.

                --token        The token to authenticate with.

                Requires the following arguments passed to the subcommand.

                --project      The variable project
                --name         The variable name

            """
            ),
            action="store",
        ),
        argument(
            "-t",
            "--type",
            help=textwrap.dedent(
                """\
                The type of variable.

                Valid options are;

                    REGULAR
                    SECRET
                    RESTRICTED

                Requires the following arguments passed globally.

                --token        The token to authenticate with.

                Requires the following arguments passed to the subcommand.

                --project      The variable project
                --name         The variable name

            """
            ),
            action="store",
        ),
        argument(
            "-v",
            "--value",
            help=textwrap.dedent(
                """\
                The contents of the variable.

                Requires the following arguments passed globally.

                --token        The token to authenticate with.

                Requires the following arguments passed to the subcommand.

                --project      The variable project
                --name         The variable name

            """
            ),
            action="store",
        ),
    ]
)
# pylint: disable=too-many-branches
# pylint: disable=too-many-statements
def variables(args=None):  # noqa: C901
    """
    Variable.

    Subcommand for working with vRA variables.
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

    vra_variable = variable.VRAVariable(
        var_project=args.project,
        var_name=args.name,
        var_desc=args.description,
        var_type=args.type,
        var_value=args.value,
    )

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

    # By convention, the bash scripts default
    # to ${CODESTREAM_CLI_VRA_TOKEN:-EMPTY} to catch empty vars.
    if args.token == "EMPTY":
        message = """
            The provided token was set to the string 'EMPTY'.
            Check the variable that was passed contains a valid token.
        """
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
    # Get variable
    ####################

    if args.get_variable:
        if config.TRACE_ENABLED:
            message = f"Processing {args.subcommand} option --get-variable"
            log.debug(message)

        # The name and project are mandatory.
        if args.name is None or args.project is None:
            CONSOLE_PARSER.print_help()
            message = "You need to provide a project and name."
            log.error(message)
            logger.eprint(message)
            return 1

        try:
            response, status_code = variable.get(
                settings=settings,
                bearer_token=bearer_token,
                variable=vra_variable,
            )

        # pylint: disable=broad-except
        except Exception as err:
            message = (
                f"An exception occurred whilst getting variable {args.name}. "
                "Enable the debug log level for further information."
            )
            log.error(message)
            log.error(err)
            return 1

        result = rest.check_status_code(status_code)

        if result:
            message = f"Displaying variable info for {args.name}"
            log.info(message)
            return_code = 0

            # Print the response to stdout.
            print(json.dumps(response, indent=4))

        else:
            return_code = 1

        return return_code

    ####################
    # Set variable
    ####################

    if args.set_variable:
        if config.TRACE_ENABLED:
            message = f"Processing {args.subcommand} option --set-variable"
            log.debug(message)

        # The name, project, type, value are mandatory.
        if (
            args.name is None
            or args.project is None
            or args.type is None
            or args.value is None
        ):
            CONSOLE_PARSER.print_help()
            message = (
                "You need to provide the following fields "
                "to update a variable. "
                "Name, Project, Type, Value."
            )
            log.error(message)
            logger.eprint(message)
            return 1

        # There are only three types of variables allowed.
        allowed_types = [
            "REGULAR",
            "SECRET",
            "RESTRICTED",
        ]
        if args.type not in allowed_types:
            message = (
                "Incorrect variable type provided. "
                "Allowed types are; REGULAR, SECRET, RESTRICTED"
            )
            log.error(message)
            logger.eprint(message)
            return 1

        try:
            response, status_code = variable.update(
                settings=settings,
                bearer_token=bearer_token,
                variable=vra_variable,
            )

        # pylint: disable=broad-except
        except Exception as err:
            message = (
                f"An exception occurred whilst getting variable {args.name}. "
                "Enable the debug log level for further information."
            )
            log.error(message)
            log.error(err)
            return 1

        result = rest.check_status_code(status_code)

        if result:
            message = f"Displaying response info for {args.name}"
            log.info(message)
            return_code = 0

            # Print the response to stdout.
            print(json.dumps(response, indent=4))

        else:
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
