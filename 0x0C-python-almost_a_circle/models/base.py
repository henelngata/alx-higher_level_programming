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
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        try:
            with open("{}.json".format(cls.__name__), 'a+') as file:
                k = 0
                lists = []
                while (k < len(list_objs)):
                    obj = list_objs[k]
                    lists.append(obj.to_dictionary())
                    k += 1
                json.dump(cls.to_json_string(lists), fp=file)
        except Exception as e:
            print("Yo have an error:{}".format(e))
