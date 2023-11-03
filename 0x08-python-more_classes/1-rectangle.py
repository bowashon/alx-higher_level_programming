#!/usr/bin/python3
"""Define a class rectangle"""


class Rectangle:
    """
    Defines a class Rectangle
    Instantiation:
        (self, width=0, height=0)
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrieves the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
