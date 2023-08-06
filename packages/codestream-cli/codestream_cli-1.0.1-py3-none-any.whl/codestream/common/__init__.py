#!/usr/bin/env python3

"""
Common module.

Common functions shared across modules.
"""

import logging
import os
import sys

from pathlib import Path

import pkg_resources
import toml
import validators

from codestream.common import config

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
#   Classes
# ---------------------------------------------------------------------------


class VRADefaultSettings:
    """
    The default settings for vRA.

    Args:
        object (class): Reusable object holding vRA default settings.
    """

    def __init__(
        self,
        version,
        insecure,
        url,
        dry_run,
        bearer_token,
        timeout,
    ):
        """
        Define default settings for vRA.

        A class defining a set of default vRA settings to pass around.

        Args:
            dry_run (bool): Whether to make changes or not.
            url (string): The vRA API URL.
            insecure (bool): Enable to ignore certificate verification.
            bearer_token (string): vRA access token.
        """
        self.version = version
        self.dry_run = dry_run
        self.url = url
        self.insecure = insecure
        self.bearer_token = bearer_token
        self.timeout = timeout


class VRASettings:
    """
    The common settings for vRA.

    Args:
        object (class): Reusable object holding vRA common settings.
    """

    def __init__(self, dry_run, url, insecure, timeout):
        """
        Define common settings for vRA.

        A class defining a set of vRA settings to pass around.

        Args:
            dry_run (bool): Whether to make changes or not.
            url (string): The vRA API URL.
            insecure (bool): Enable to ignore certificate verification.
            bearer_token (string): vRA access token.
        """
        self.dry_run = dry_run
        self.url = url
        self.insecure = insecure
        self.timeout = timeout


# ---------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------


def get_version():
    """
    Get the version number.

    Determine the version number or set a default value as a fallback.
    """
    name_function = whoami(option="function")
    name_caller = whoami(option="caller")
    if config.TRACE_ENABLED:
        log.debug("Entering %s from %s", name_function, name_caller)

    try:
        log.debug("Attempting to obtain version from installed package")
        version = pkg_resources.get_distribution(config.PACKAGE_NAME).version

    except pkg_resources.DistributionNotFound:
        try:
            log.debug("Falling back to parsing pyproject.toml")
            root = Path(__file__).parent.parent.parent.parent
            path_file = os.path.join(root, "pyproject.toml")

            log.debug("Reading file %s", path_file)
            with open(file=path_file, mode="rt", encoding="utf-8") as file:
                data = toml.load(file)
                version = data["project"]["version"]

        except Exception:
            log.debug("Falling back to default version")
            version = "0.0.0"

        finally:
            file.close()

    return version


def whoami(option="function"):
    """
    Who Am I.

    Inputs:
        option: String can be "function" or "caller"

    Returns:
        string: The name of the function.
    """
    if option == "function":
        result = sys._getframe(1).f_code.co_name
    elif option == "caller":
        result = sys._getframe(2).f_code.co_name
    else:
        result = f"unknown option {option}"

    return result


def validate_url(url=str):
    """
    Validate URL.

    A quick hack to ensure a url a URL is valid.
    """
    # If empty,
    if url is None:
        reason = "Value provided was none."
        result = False

    # If less then min characters
    elif len(url) < 4:
        reason = "Value was less than required chars."
        result = False

    # If it fails the validator.
    elif not validators.url(url):
        reason = "Failed URL validator"
        result = False

    # If it passes the validator.
    elif validators.url(url):
        result = True

    if result:
        # LGTM, passes all currently performed tests.
        log.info("Valid URL %s", url)
        return True

    # Failed one or more tests.
    log.error("An invalid URL was provided. URL: %s Reason: %s", url, reason)
    return False
