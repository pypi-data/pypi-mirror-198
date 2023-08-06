#!/usr/bin/env python3

"""
Doco module.

Functions for serving sphinx generated documentation via flask.
"""

import logging
from pathlib import Path

from flask import Flask, send_from_directory

from codestream.common import config, logger, files, exceptions, whoami

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------


def run(dry_run, directory, port):
    """
    Run.

    Run the doco module.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # Make sure the directory actually exists.
    try:
        full_path = Path(files.get_full_path(path=directory))

        if full_path.is_dir():
            log.debug("The path exists %s", full_path)
        else:
            message = f"The provided path {full_path} does not exist."
            raise FileExistsError(message)

    except FileExistsError as err:
        message = "Unable to serve docs from non-existent directory."
        log.error(message)
        log.error(err)
        logger.eprint(message)
        raise FileExistsError from err

    except Exception as err:
        message = "Unhandled exception serving documentation."
        log.error(message)
        log.error(err)
        raise Exception from err

    if 1024 <= int(port) <= 65535:
        log.debug("The port %s is in the allowed range", port)
    else:
        message = f"The port {port} is outside the allowed range of 1024-65535"
        log.error(message)
        logger.eprint(message)
        raise exceptions.PortOutOfRange(port)

    # If dry run is enabled, nothing is executed.
    if dry_run:
        text = (
            "DRY RUN ENABLED\n" f"DIRECTORY: {directory}\n" f"PORT: {port}\n"
        )
        logger.eprint(text)

    else:
        try:
            serve(full_path, port)

        except Exception as err:
            message = "Unhandled exception serving documentation."
            log.error(message)
            log.error(err)
            raise


def serve(directory, port):
    """
    Serve the docs.

    Serves the HTML docs generated with Sphinx using Flask.

    When run outside a container can override the port and folder.
    """
    log.debug("Entering %s", __name__)

    app = Flask(__name__)

    # Handle the homepage
    @app.route("/", methods=["GET"])
    def flask_index():
        return send_from_directory(directory, "index.html")

    # Handle all links
    @app.route("/<path:path>", methods=["GET"])
    def flask_links(path):
        return send_from_directory(directory, path)

    try:
        # Ignore the bandit sec warnings as this is only ever run locally.
        app.run(
            host="0.0.0.0",  # nosec B104
            port=port,
            debug=True,  # nosec B201
            use_debugger=False,
            use_reloader=False,
        )

    except Exception as err:
        message = (
            f"Unhandled exception when serving docs "
            f"from {directory} "
            f"on port {port}"
        )
        log.error(message)
        log.error(err)
        raise Exception from err
