#!/usr/bin/python3
"""Create a class Squre """


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """initiates the class"""
        self.size = size

    @property
    def size(self):
        """Retrieve the size"""
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
        """Calculate and return the area"""
        return self.__size * self.__size
