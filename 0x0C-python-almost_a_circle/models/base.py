#!/usr/bin/python3

"""This class will be the “base” of all other classes in this project.
"""
import json


class Base:
    """
    Args:
        __nb_objects: private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
