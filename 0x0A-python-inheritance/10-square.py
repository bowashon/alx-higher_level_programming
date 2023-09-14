#!/usr/bin/python3
"""Defines a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square that inherits from Rectangle"""
    def __init__(self, size):
        """
        instantiate: instantiate the Square
        Args:
        size: the size of the Square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Defines the area of the Square"""
        return self.__size * self.__size
