#!/usr/bin/python3

"""Write a function that creates
an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """
    Args:
        filename: a file that contains the json
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
