#!/usr/bin/env python3

"""
File module.

Reusable functions for working files.
"""

import logging
import os

from codestream.common import config, whoami

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------


def get_full_path(path):
    """
    Get the full path.

    Returns the full path to a relative directory provided.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    try:
        full_path = os.path.abspath(path)

    except Exception as err:
        log.error("Unhandled exception obtaining path for %s", path)
        log.error(err)
        raise Exception from err

    if config.TRACE_ENABLED:
        log.debug("Set full_path to %s", full_path)

    return full_path


def read_yaml_file(file):
    """
    Read a YAML file.

    Returns a file stream after ensuring it's valid YAML.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    try:
        with open(file=file, mode="rt", encoding="utf-8") as stream:
            file_stream = stream.read()

    except OSError as err:
        log.error("Failed to open file %s in read-only mode", file)
        log.error(err)
        raise Exception from err

    except Exception as err:
        log.error("Unhandled exception opening file %s", file)
        log.error(err)
        raise Exception from err

    finally:
        stream.close()

    # TODO: Add a YAML validation check here.

    return file_stream


def write_yaml_file(contents, file):
    """
    Write a YAML file.

    Writes a file stream after ensuring it's valid YAML.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    # TODO: Add a YAML validation check here.
    # ... contents

    try:
        with open(file=file, mode="w", encoding="utf-8") as stream:
            stream.write(contents)

    except OSError as err:
        log.error("Failed to open file %s in write mode", file)
        log.error(err)
        raise Exception from err

    except Exception as err:
        log.error("Unhandled exception opening file %s", file)
        log.error(err)
        raise Exception from err

    finally:
        stream.close()

    return 0
