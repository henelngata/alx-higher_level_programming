#!/usr/bin/python3

""" contains a function
that returns True if the object is an instance of
or if the object is an instance of a class that inherited from,
the specified class;
otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    args:
        obj: object to be compared
        a_class: to get if a object belongs to
    Returns:
            True or Flase from
    """
    return isinstance(obj, a_class)
