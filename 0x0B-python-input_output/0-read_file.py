#!/usr/bin/python3
"""Function that reads a text file"""


def read_file(filename=""):
    """
    Definiition: 
        funtion that reads a text file in (UTF8)
    Args:
        filename: the name of the file provided
    Prints to the stdout the content of the file
    """

    with open(filename, 'r', encoding='UTF-8') as f:
        read_data = f.read()
        print(read_data, end="")
