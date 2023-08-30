#!/usr/bin/python3
"""Create class with attributes, setter and getter"""


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        self.__size = size
        """initialize
        parameters
        -----------
        size:int, optional
        """
    @property
    def size(self):
        """ Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#' characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
