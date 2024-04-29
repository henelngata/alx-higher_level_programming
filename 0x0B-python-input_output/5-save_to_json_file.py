#!/usr/bin/python3

"""Write a function that writes an Object
to a text file
using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """
    args:
        my_obj: The object to be writen
        filename: The file to write the obj
    """
    with open(filename, "w+", encoding="utf-8") as f:
        json.dump(my_obj, f)
