#!/usr/bin/python3
""" This module contains a class MyList tha inherits
from LIst
"""


class MyList(list):
    """This class MyList"""

    def print_sorted(self):
        my_list = list(self)
        my_list.sort()
        print("{}".format(my_list))
