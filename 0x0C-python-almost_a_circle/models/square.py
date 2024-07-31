#!/usr/bin/python3

""" Imports class Rectangle from Rectangle module"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Class square inherites its attributes and behavior form rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    def __str__(self) -> str:
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)