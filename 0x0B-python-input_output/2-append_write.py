#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """
    Definition:
        Defines a function that appends a string at the end of a text file
    Args:
        filename: a string that represents the name of the file
        text: a string content of the file
    Return:
        return the number of characters written
    """

    with open(filename, "a", encoding='UTF-8') as f:
        return f.write(text)
