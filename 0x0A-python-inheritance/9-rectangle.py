#!/usr/bin/python3
"""Conatains an empty class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle (BaseGeometry):
    """
    An empty class
    """
    def __init__(self, width, height):
        """
        args:
            width: int the width
            height: int the height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns:
        the string rep of this class
        """
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width,
                                   self.__height)
