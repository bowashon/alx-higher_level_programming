#!/usr/bin/python3
"""Function that prints a square with the character"""

def print_square(size):
    """
    Definition:
        Defines a function that prints square with #
    Arg:
        size: represents the size of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    i = 0
    while i < size:
        j = 0
        while j < size:
            print("#", end='')
            j += 1
        print()
        i += 1
