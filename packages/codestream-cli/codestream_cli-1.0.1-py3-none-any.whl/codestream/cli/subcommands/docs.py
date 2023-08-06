#!/usr/bin/env python3

"""
Docs.

Argument handling for the 'docs' subcommand.
"""

import logging
import textwrap

from codestream.common import config, whoami
from codestream.cli.subcommands import subcommand, argument

from codestream import doco

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Subcommand: Docs
# ---------------------------------------------------------------------------


@subcommand(
    [
        argument(
            "-p",
            "--port",
            help=textwrap.dedent(
                """\

                The Port.

                Specifies the port to serve the docs on.

                Note that this is only useful when run locally, as when run
                inside a container, the port is already exposed on the default.

            """
            ),
            action="store",
            default="5000",
        ),
        argument(
            "-d",
            "--directory",
            help=textwrap.dedent(
                """\

                The directory to serve the docs from.

                This directory needs to already exist or an
                error will be thrown.

            """
            ),
            action="store",
            default="/srv",
        ),
    ]
)
def docs(args=None):
    """
    Docs.

    Subcommand to serve the sphinx documentation on localhost.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)
        log.debug(args)

    try:
        doco.run(
            dry_run=args.dry_run, directory=args.directory, port=args.port
        )

    except Exception as err:
        message = (
            "An exception occurred when attempting to serve the documentation."
        )
        log.error(message)
        log.error(err)
        return 1

    return 0
