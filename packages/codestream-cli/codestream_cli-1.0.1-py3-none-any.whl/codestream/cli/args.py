#!/usr/bin/env python3

"""
Args module.

Parsing of command line arguments.

Usage:

    from codestream.cli.args import CONSOLE_ARGS
"""

import argparse
import logging

import argcomplete

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Initialisations
# ---------------------------------------------------------------------------

CONSOLE_PARSER = None
CONSOLE_SUBPARSER = None

# ---------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------


def _parse_arguments():
    parser = argparse.ArgumentParser(
        prog="codestream-cli",
        description="vRA utilities",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    subparsers = parser.add_subparsers(
        help="subcommand help",
        dest="subcommand",
    )

    argcomplete.autocomplete(parser)

    return parser, subparsers


# ---------------------------------------------------------------------------
#   Constants
# ---------------------------------------------------------------------------

CONSOLE_PARSER, CONSOLE_SUBPARSER = _parse_arguments()

# Delete the function to avoid accidental usage.
del _parse_arguments
