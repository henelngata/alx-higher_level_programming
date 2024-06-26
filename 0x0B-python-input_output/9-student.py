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

    def to_json(self):
        """
        retrieves a dictionary representation of a Student
        Returns:
                Dictionary
        """
        return self.__dict__
