#!/usr/bin/python3
"""Conatains an empty class
"""


class BaseGeometry:
    """
    An empty class
    """
    def area(self):
        """
        that raises an Exception with the
        message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value

        args:
            name(string): string
            value(int): value to be validated
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
