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
        try:
            super().integer_validator("width", width)
            super().integer_validator("height", height)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
        else:
            self.__width = width
            self.__height = height
