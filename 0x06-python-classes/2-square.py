#!/usr/bin/python3
"""create a class Square with attributes and instantiation with raise Errors"""


class Square:
    """A class to represent a square"""
    def __init__(self, size=0):
        """initialize the squre"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
