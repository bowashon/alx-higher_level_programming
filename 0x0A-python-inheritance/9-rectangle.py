#!/usr/bin/python3
""" A Rectangle class that inherite from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a class Rectangle that inherits from
    class BaseGeometry in 7-base_geometry model
    """

    def __init__(self, width, height):
        """
        instantiate the width and the height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[{}] {}/{}".format(self.__class__.__name__,
                self.__width, self.__height))
