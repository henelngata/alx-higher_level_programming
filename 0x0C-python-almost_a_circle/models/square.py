#!/usr/bin/python3

""" Imports class Rectangle from Rectangle module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square inherites its attributes and behavior form rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """Return string rep of the class"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        """ gets the value of width"""
        return self.width

    @size.setter
    def size(self, value):
        """ sets the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
