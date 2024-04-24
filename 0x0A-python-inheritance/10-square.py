#!/usr/bin/python3

"""This module contains class Square"""

Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """ Class rectangle"""

    def __init__(self, size):
        """Instantiation with
        """
        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        """returns the area of A square
        """
        return ((self.__size * self.__size))
