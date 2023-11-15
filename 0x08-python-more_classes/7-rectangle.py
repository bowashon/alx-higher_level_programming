#!/usr/bin/python3
"""Defines a class rectangle"""


class Rectangle:
    """Defines a class rectangle
    instantiate(self, width=0, height=0)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ instantiate the the rectangle"""
        self.__width = width
        self.__height = height
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
        self.__widht = value

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
        self.__height = value

    def area(self):
        """Public instance method"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method perimeter"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """print the rectangle"""
        rectangle_str = ""
        if self.__width != 0 or self.__height != 0:
            return ((str(self.print_symbol) * self.width + '\n')
                    * self.height)[:-1]
        else:
            return ""

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
