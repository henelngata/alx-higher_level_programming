#!/usr/bin/python3

"""a class Student that defines a student by:
"""


class Student:
    """a class Student that defines a student by:
    Args:
        first_name(string)
        last_name(string)
        age(int)
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student
        Returns:
                Dictionary
        """
        if attrs is None:
            return self.__dict__
        else:
            atts = {}

            for att in attrs:
                try:
                    atts.update({att: getattr(self, att)})
                except AttributeError:
                    pass
            return atts

    def reload_from_json(self, json):
        """
        that replaces all attributes of the Student
        """
        self.__dict__.update(json)
