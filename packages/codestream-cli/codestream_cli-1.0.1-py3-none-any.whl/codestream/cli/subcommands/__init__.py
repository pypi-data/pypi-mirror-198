#!/usr/bin/env python3

"""
Subcommands module.

Submodule for handling arguments to subcommands.
"""

import argparse
import logging

from codestream.cli.args import CONSOLE_SUBPARSER
from codestream.common import config, whoami

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Mutually exclusive
# ---------------------------------------------------------------------------


# Commands in this list are mutually exclusive with each other.
# TODO: Fix mutually exclusive commands.
mutually_exclusive = [
    "-cp",
    "--check-pipeline",
    "-gp",
    "--get-pipeline",
    "-gpid",
    "--get-pipeline-id",
    "-up",
    "--upload-pipeline",
    "-dp",
    "--download-pipeline",
    "-delp",
    "--delete-pipeline",
    "-ep",
    "--enable-pipeline",
    "-rp",
    "--run-pipeline",
    "-gd",
    "--get-deployment",
    "--deld",
    "--delete-deployment",
    "-ld",
    "--lint-blueprint",
]

# ---------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------


def parse_extra(parser, namespace):
    """
    Parse extra.

    Take the 'extra' attribute from the global namespace and
    re-parse it to create separate namespaces for all other subcommands.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    namespaces = []
    extra = namespace.extra

    while extra:
        n = parser.parse_args(extra)
        extra = n.extra
        namespaces.append(n)

    return namespaces


def argument(*name_or_flags, **kwargs):
    """
    Argument is a convenience function.

    Used to properly format arguments to pass to the subcommand decorator.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    return (list(name_or_flags), kwargs)


def subcommand(args=None, parent=CONSOLE_SUBPARSER):
    """
    Define a new subcommand.

    A decorator to define a new subcommand in a sanity-preserving way.

    The function will be stored in the ``func`` variable when the parser
    parses arguments so that it can be called directly like this example.

    Usage example::

        args = parser.parse_args()
        args.func(args)

    Usage example::

        @subcommand(
            [
                argument(
                    "-d",
                    "--debug",
                    help="Enable debug mode",
                    action="store_true"
                )
            ]
        )
        def subcommand(args):
            print(args)

    Then on the command line::

        $ python cli.py subcommand -d
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    if args is None:
        args = []

    def decorator(func):
        parser = parent.add_parser(
            func.__name__,
            description=func.__doc__,
            formatter_class=argparse.RawTextHelpFormatter,
        )

        for arg in args:
            me_match = list(set(arg[0]).intersection(set(mutually_exclusive)))

            if me_match:
                parser.add_mutually_exclusive_group(
                    required=False
                ).add_argument(*arg[0], **arg[1])
                parser.set_defaults(func=func)

            else:
                parser.add_argument(*arg[0], **arg[1])
                parser.set_defaults(func=func)

    return decorator
