#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """Defines a class Rectangle"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Attribute that reteive the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """attributs that sets the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value >= 0:
            raise ValueError("value must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Attribute that retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height value of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif height >= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Defines the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Defines the perimeter of the rectangle"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Defines string for printing the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        rectangle_str += "\n".join("#" * self.__width
                                   for i in range(self.__height))
        return rectangle_str

    def __repr__(self):
        """Defines the string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance of a class
           is deleted
        """
        print("Bye rectangle...")
