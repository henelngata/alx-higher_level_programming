#!/usr/bin/python3

"""write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """
    args:
        filename: file to be written
        text: test to be written
    """
    with open(filename, "w", encoding="utf-8") as f:
        num_of_char = f.write(text)
    return num_of_char
