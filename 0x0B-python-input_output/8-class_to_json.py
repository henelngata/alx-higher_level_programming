#!/usr/bin/python3

"""a function that returns the dictionary
description with simple data structure
"""


def class_to_json(obj):
    """
    Args:
        obj:is an instance of a Class
    """
    return obj.__dict__
