#!/usr/bin/python3
"""Defines a class rectangle"""


class Rectangle:
    """Defines a class rectangle
    instantiate(self, width=0, height=0)
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ instantiate the the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be  >= 0")

    @property
    def height(self):
        """ returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Public instance method"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method perimeter"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """print the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        if self.__width != 0 and self.__height != 0:
            rectangle_str += "\n" .join("#" * self.__width
                                        for i in range(self.__height))

    def __repr__(self):
        print("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
