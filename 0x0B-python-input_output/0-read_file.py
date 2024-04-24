#!/usr/bin/python3
"""contains a function read_file
"""


def read_file(filename=""):
    """
    args:
        filename: file to be read
    """
    with open(filename, "r", encoding="utf-8") as f:
        read_obj = f.read()
        print("{}".format(read_obj))
