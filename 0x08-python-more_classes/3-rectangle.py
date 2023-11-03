#!/usr/bin/python3
"""Define a class rectangle"""


class Rectangle:
    """
    Defines a class Rectangle
    Instantiation:
        (self, width=0, height=0)
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        retrieves the width
        """
        return self.width

    @setter
    def width(self, value):
        """sets the width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return self.__height

    @setter
    def height(self, value):
        """sets the value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.widht * self.height)
