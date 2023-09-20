#!/usr/bin/python3
"""Function that prinst as square with character #"""


def print_square(size):
    """
    Definition: Defines a function that prints square
    
    Args: 
        size: is the length of the square
    """
    if not isinstance(size, int):
        raise TypeError("sizee must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    i = 0
    while i < size:
        for j in range(size):
            print("#", end='')
        print('')
        i += 1
