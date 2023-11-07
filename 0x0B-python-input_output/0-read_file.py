#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """
    function that reads a text file(UTF8)
    prints - prints to the stdout
    """
    with open(filename, 'r', encoding="UTF8") as f:
        read_file = f.read()
        print(read_file, end='')
