#!/usr/bin/env python3

"""
Config module.

Holds config related stuff.
"""

import logging
import os

log = logging.getLogger(__name__)

# The main package name, not the module name.
PACKAGE_NAME = "codestream-cli"

# Enable in conjunction with debug logs for request tracing.
TRACE_ENABLED = (
    os.getenv("CODESTREAM_CLI_TRACE_ENABLED", "FALSE").upper() == "TRUE"
)
