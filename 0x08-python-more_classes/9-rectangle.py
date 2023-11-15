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
        self.__width = value

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """
        returns a new Rectangle instance with
        width == height == size
        """
        return cls(size, size)
