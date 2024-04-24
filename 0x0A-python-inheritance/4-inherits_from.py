#!/usr/bin/python3

"""This module contains
that returns True if the object is an instance of a class
"""


def inherits_from(obj, a_class):
    """
    args:
        obj: The object of a class
        a_class: The class
    Returns:
        True or False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

