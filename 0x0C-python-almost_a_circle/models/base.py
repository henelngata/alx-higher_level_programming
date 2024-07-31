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
        """Writes the JSON string representation of list_objs to a file."""
        filename = f"{cls.__name__}.json"
        list_dicts = ([obj.to_dictionary() for obj in list_objs]
                      if list_objs else [])
        json_string = cls.to_json_string(list_dicts)

        try:
            with open(filename, 'w') as file:
                file.write(json_string)
        except IOError as e:
            print(f"Error: {e}")

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 2, 2)
        dummy.update(**dictionary)
        return dummy
