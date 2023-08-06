#!/usr/bin/env python3

"""
Blueprints.

Argument handling for the 'blueprints' subcommand.
"""

import logging
import os
import textwrap

from codestream.cli.args import CONSOLE_PARSER
from codestream.common import config, logger, VRASettings, whoami
from codestream.cli.subcommands import subcommand, argument

from codestream.api import blueprint

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Subcommand: Blueprint
# ---------------------------------------------------------------------------


@subcommand(
    [
        argument(
            "-l",
            "--lint-blueprint",
            help=textwrap.dedent(
                """\

                Lint a provided vRA Blueprint.

                Requires the following arguments passed to the subcommand.

                --file              The path to the YAML blueprint.

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
    ]
)
def blueprints(args=None):
    """
    Blueprints.

    Subcommand for working with vRA Blueprints.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)
        log.debug(args)

    ####################
    # Settings
    ####################

    settings = VRASettings(
        dry_run=args.dry_run,
        url=None,
        insecure=args.insecure,
        timeout=args.timeout,
    )

    ####################
    # Lint Blueprint
    ####################

    if args.lint_blueprint:
        if config.TRACE_ENABLED:
            log.debug(
                "Processing %s option --lint-deployment", args.subcommand
            )

        if args.file is None:
            CONSOLE_PARSER.print_help()
            log.error("You forgot to provide a file name. ")
            return 1

        if not os.path.exists(args.file):
            log.error("The file %s does not exist", args.file)
            return 1

        try:
            result = blueprint.lint(
                settings=settings,
                file=args.file,
            )

        except Exception as err:
            message = (
                "An exception occurred whilst linting blueprint {args.file}. "
                "Enable the debug log level for further information."
            )
            log.error(message)
            log.error(err)
            return 1

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
