#!/usr/bin/python3

"""This class will be the “base” of all other classes in this project.
"""


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
