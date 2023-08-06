#!/usr/bin/env python3

"""
Exceptions module.

Custom exceptions.
"""

# ---------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------


class PortOutOfRange(Exception):
    """
    PortOutOfRange exception.

    Custom exception for when a provided port is out of the allowed range.
    """

    def __init__(self, port):
        """
        Message method.

        Method to allow custom message printing.
        """
        message = f"The port {port} is outside the allowed range of 1024-65535"

        super().__init__(message)


class ApiExceptionGitLab(Exception):
    """
    ApiException.

    A generic exception for handling GitLab status codes.
    """

    def __init__(self, status_code):
        """
        Message method.

        Method to allow custom message printing.
        """
        if status_code == 403:
            message = "Rate limit reached. Please wait a minute and try again."
        else:
            message = f"HTTP Status Code was: {status_code}."

        super().__init__(message)


class ApiExceptionVRA(Exception):
    """
    ApiException.

    A generic exception for handling vRA status codes.
    """

    def __init__(self, status_code):
        """
        Message method.

        Method to allow custom message printing.
        """
        # Need python > 3.10 for match. :(

        if status_code == 401:
            message = f"{status_code} Unauthorized Request"

        elif status_code == 403:
            message = f"{status_code} Forbidden Request"

        elif status_code == 404:
            message = f"{status_code} Not Found"

        elif status_code == 500:
            message = f"{status_code} Server Side error"

        else:
            message = f"{status_code} Unhandled error status."

        super().__init__(message)
