"""This module contains a function lookup(obj)
"""


def lookup(obj):
    """
    Args:
        obj(object): This an object
    Returns:
            a list object
    """
    return obj.__dict__
