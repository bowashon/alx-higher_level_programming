#!/usr/bin/python3
"""create square with attributes, private instance and public instance"""


class Square:
    """A class represent a square."""
    def __init__(self, size=0):
        """
        Attributes
        ---------
        size : int - the size of the square.

       """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate and return the area"""
        return self.__size * self.__size
