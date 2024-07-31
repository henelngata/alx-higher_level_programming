#!/usr/bin/python3

""" Imports class Base from base module"""

from models.base import Base


class Rectangle(Base):
    """ Has no attributes """

    def __init__(self, width, height, x=0, y=0, id=None):

        """ Initializes instances of class rectangle
        Attributes:
            width(int): private attribute width
            height(int): private attribute height
            x:private attr
            y:private attr
        """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """ gets the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ gets the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ gets the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """ sets the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ gets the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ sets the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle class (width * height)"""
        return (self.__height * self.__width)

    def display(self):
        """prints in stdout the Rectangle instance with the character #
        """
        i = 0
        while (i < self.__height):
            j = 0
            while (j < self.__width):
                print("{}".format("#"), end="")
                j += 1
            print()
            i += 1

    def __str__(self) -> str:
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)
