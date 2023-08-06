#!/usr/bin/env python3

"""
Command module.

Functions for handling arguments to the main command.
"""

import logging
import os
import textwrap

from codestream.cli.args import CONSOLE_PARSER
from codestream.common import (
    config,
    logger,
    get_version,
    VRADefaultSettings,
    whoami,
)

from codestream.cli.subcommands import (
    # blueprints,       # TODO: Finish this subcommand.
    # deployments,      # TODO: Finish this subcommand.
    docs,
    pipelines,
    token,
    variables,
)  # noqa: F401

__all__ = [
    "entrypoint",
    # "blueprints",     # TODO: Finish this subcommand.
    # "deployments",    # TODO: Finish this subcommand.
    "docs",
    "pipelines",
    "token",
    "variables",
]

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------


def entrypoint():
    """
    CLI entrypoint.

    The entrypoint into all CLI options and subcommands.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    try:
        defaults = load_default_settings()

    except Exception as err:
        log.error("Unhandled exception loading default settings")
        log.error(err)
        raise Exception from err

    # Parse command
    try:
        args = parse_arguments(
            settings=defaults,
        )

    except Exception as err:
        log.error("Unhandled exception parsing CLI arguments")
        log.error(err)
        raise Exception from err

    try:
        if args.subcommand is None:
            CONSOLE_PARSER.print_help()
            logger.eprint(
                "Please provide a subcommand from the options below."
            )
            return 1

    except AttributeError:
        CONSOLE_PARSER.print_help()
        logger.eprint(
            "Attribute error. Please provide a subcommand from the options below."
        )
        return 1

    log.debug("Processing subcommand %s", args.subcommand)
    return args.func(args)


def load_default_settings():
    """
    Load vRA default settings.

    Loads settings from the environment or sets a default when not present.

    The following environment variables can be overridden by passed CLI args.

    Variables::

        Name: CODESTREAM_CLI_SKIP_VERIFY_CERTS
        Default: Defaults to False.
        Override: Set to 'TRUE' to disable certificate verification.

        Name: CODESTREAM_CLI_VRA_URL
        Default: Defaults to None.
        Override: Set to the URL of your vRA API

        Name: CODESTREAM_CLI_DRY_RUN
        Default: Defaults to False
        Override: Set to 'TRUE' to enable dry run and no changes are made.

        Name: CODESTREAM_CLI_VRA_TIMEOUT
        Default: Defaults to 5 seconds.
        Override: Set to an integer to increase or decrease the API timeout.

        Name: CODESTREAM_CLI_VRA_TOKEN
        Default: Defaults to None
        Override: Set to a valid Refresh Token to avoid requiring "--token"
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    settings_dict = {}

    # Get the version number of the script.
    setting_version = get_version()
    settings_dict["version"] = setting_version

    # Disable certificate verification if required
    setting_verify_certs = (
        os.getenv("CODESTREAM_CLI_SKIP_VERIFY_CERTS", "FALSE").upper()
        == "TRUE"
    )
    settings_dict["insecure"] = setting_verify_certs

    # Try and get the vRA URL from the environment first or set a default.
    setting_vra_url = os.getenv("CODESTREAM_CLI_VRA_URL")
    settings_dict["url"] = setting_vra_url

    # The default vRA API timeout.
    setting_timeout = os.getenv("CODESTREAM_CLI_VRA_TIMEOUT", "5")
    settings_dict["timeout"] = setting_timeout

    # Enable dry run mode.
    setting_dry_run = (
        os.getenv("CODESTREAM_CLI_DRY_RUN", "FALSE").upper() == "TRUE"
    )
    settings_dict["dry_run"] = setting_dry_run

    # vRA Token
    setting_vra_token = os.getenv("CODESTREAM_CLI_VRA_TOKEN")
    settings_dict["vra_token"] = setting_vra_token

    settings_obj = VRADefaultSettings(
        version=setting_version,
        insecure=setting_verify_certs,
        url=setting_vra_url,
        dry_run=setting_dry_run,
        bearer_token=setting_vra_token,
        timeout=int(setting_timeout),
    )

    log.debug(settings_obj)

    # return settings_dict
    return settings_obj


def parse_arguments(settings=VRADefaultSettings):
    """
    Create an argument parser.

    Creates an argument parser capable of handling subcommands.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # Add these arguments to the root level parser.

    # Version
    CONSOLE_PARSER.add_argument(
        "-v",
        "--version",
        help=textwrap.dedent(
            """\
            Print the version and exit.
            """
        ),
        action="version",
        version=settings.version,
    )

    # vRA URL
    CONSOLE_PARSER.add_argument(
        "-url",
        "--url",
        help=textwrap.dedent(
            """\
            The vRA URL.
            """
        ),
        action="store",
        default=settings.url,
    )

    # Disable TLS verification
    CONSOLE_PARSER.add_argument(
        "-k",
        "--insecure",
        help=textwrap.dedent(
            """\
            Disable TLS verification.

            Ignores all self-signed and untrusted certificates.
            """
        ),
        action="store_true",
        default=settings.insecure,
    )

    # Enable dry run
    CONSOLE_PARSER.add_argument(
        "-dry",
        "--dry-run",
        help=textwrap.dedent(
            """\
            Activate dry run mode.

            In this mode all commands will be displayed on screen.

            No changes will be made.
            """
        ),
        action="store_true",
        default=settings.dry_run,
    )

    # vRA API Timeout
    CONSOLE_PARSER.add_argument(
        "-time",
        "--timeout",
        help=textwrap.dedent(
            """\
            The timeout to wait for the vRA API to return.

            Defaults to a very lenient 5 seconds.
            """
        ),
        action="store",
        default=settings.timeout,
    )

    # vRA Token
    CONSOLE_PARSER.add_argument(
        "-t",
        "--token",
        help=textwrap.dedent(
            """\
            The Token use for authenticating with the vRA API.

            This is mandatory for all 'pipeline' and 'blueprint' subcommands.

            To obtain a Token, look at 'codestream-cli token --help'.
            """
        ),
        action="store",
        default=settings.bearer_token,
    )

    try:
        args = CONSOLE_PARSER.parse_args(
            args=None,
            namespace=None,
        )

    except Exception as err:
        log.error("Unhandled exception parsing root level arguments")
        log.error(err)
        raise Exception from err

    return args
