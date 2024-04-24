#!/usr/bin/python3

"""This module contains a function
"""


def is_same_class(obj, a_class):
    """
    args:
        obj(object): an object
        a_class(class): a class
    Returns:
            True if type(obj) is a_class
            False type(obj) is not a_class
    """
    return type(obj) is a_class
