#!/usr/bin/python3

"""From JSON string to Object
"""
import json


def from_json_string(my_str):
    """
    arg:
        my_str: the string to convert to python Data structure
    Returns:
            an object (Python data structure) represented by a JSON string:
    """
    return json.loads(my_str)
