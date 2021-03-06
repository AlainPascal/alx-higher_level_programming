#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Prints an integer

    Args:
        value: to be printed if it is integer

    Returns:
        True if value is integer, False otherwise
    """
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
    else:
        return (True)
