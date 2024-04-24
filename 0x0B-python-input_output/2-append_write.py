#!/usr/bin/python3

"""  Append to a file
"""


def append_write(filename="", text=""):
    """
    args:
        filename: file to write to
        text: text to append
    """
    with open(filename, 'a', encoding='utf-8') as f:
        num = f.write(text)
    return num
