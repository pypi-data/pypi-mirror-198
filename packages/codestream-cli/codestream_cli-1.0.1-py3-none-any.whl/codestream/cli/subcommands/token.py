#!/usr/bin/env python3

"""
Token.

Argument handling for the 'token' subcommand.
"""

import logging
import textwrap

import getpass

from codestream.cli.args import CONSOLE_PARSER
from codestream.common import config, logger, rest
from codestream.common import validate_url, VRASettings, whoami
from codestream.cli.subcommands import subcommand, argument

from codestream.api.auth import get_refresh_token, get_bearer_token

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Subcommand: Token
# ---------------------------------------------------------------------------


@subcommand(
    [
        argument(
            "-rt",
            "--refresh-token",
            help=textwrap.dedent(
                """\

                Get a refresh token

                Requires the following arguments passed globally.

                --url                The URL for the vRA API

                Requires the following arguments passed to the subcommand.

                --username           The username
                --password           The password

            """
            ),
            action="store_true",
        ),
        argument(
            "-bt",
            "--bearer-token",
            help=textwrap.dedent(
                """\

                Get a bearer access token

                NOTE: This is mostly used for debugging auth issues.

                Requires the following arguments passed globally.

                --url               The URL for the vRA API
                --token             The refresh token

                Requires the following arguments passed to the subcommand.

                None

            """
            ),
            action="store_true",
        ),
        # fmt: off
        argument(
            "-u",
            "--username",
            help="The username to get a Token for.",
            action="store"
        ),
        argument(
            "-p",
            "--password",
            help="The password for the user.",
            action="store"
        ),
        # fmt: on
    ]
)
def token(args=None):
    """
    Token.

    Subcommand for obtaining a vRA token by providing a username and password.
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
    # Refresh Token
    ####################

    if args.refresh_token:
        if config.TRACE_ENABLED:
            message = f"Processing {args.subcommand} option --refresh-token"
            log.debug(message)

        # If no username was provided, show help.
        if args.username is None:
            CONSOLE_PARSER.print_help()
            message = (
                "No username was provided! "
                "Try running 'codestream-cli token --help' for more info."
            )
            log.error(message)
            logger.eprint(message)
            return 1

        username = args.username

        # If a password wasn't provided, ask for one.
        if args.password is None:
            logger.eprint("Enter a password to access vRA: ")
            password = getpass.getpass(prompt="Password: ", stream=None)

        else:
            password = args.password

        try:
            # Obtain a refresh token by using the
            # provided username and password.
            refresh_token, status_code = get_refresh_token(
                settings=settings,
                username=username,
                password=password,
            )

        except Exception as err:
            message = (
                "An exception occurred when attempting to "
                "obtain a refresh token."
            )
            log.error(message)
            log.error(err)
            logger.eprint(message)
            return 1

        result = rest.check_status_code(status_code)

        if result:
            return_code = 0

            message = "Displaying refresh token"
            log.info(message)

            # Print the token to stdout
            # so it can be captured in downstream scripts.
            print(refresh_token)

        else:
            return_code = 1

            if status_code == 400:
                message = "Invalid username or password"
            else:
                message = (
                    f"Unknown status code received from API {status_code}"
                )

            log.error(message)
            logger.eprint(message)

        return return_code

    ####################
    # Bearer Token
    ####################

    if args.bearer_token:
        if config.TRACE_ENABLED:
            message = f"Processing {args.subcommand} option --bearer-token"
            log.debug(message)

        # If no token was provided, show help.
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
            # Obtain a refresh token by using the
            # provided username and password.
            bearer_token, status_code = get_bearer_token(
                settings=settings,
                refresh_token=args.token,
            )

        except Exception as err:
            message = (
                "An exception occurred when attempting "
                " to obtain a bearer token."
            )
            log.error(message)
            log.error(err)
            return 1

        result = rest.check_status_code(status_code)

        if result:
            return_code = 0

            message = "Displaying bearer token"
            log.info(message)

            # Print the token to stdout so it can
            # be captured in downstream scripts.
            print(bearer_token)

        else:
            return_code = 1

            if status_code == 400:
                message = "Invalid request, bad data."
            elif status_code == 403:
                message = "Forbidden."
            else:
                message = (
                    f"Unknown status code received from API {status_code}"
                )

            log.error(message)
            logger.eprint(message)

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
