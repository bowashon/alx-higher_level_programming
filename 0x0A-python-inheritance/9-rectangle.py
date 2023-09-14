#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a class rectangle that inherites from BaseGeometry"""

    def __init__(self, width, height):
        """
        instantiate(self)
        -----------
        Args:
        width: the width of the rectangle
        height: the height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """method that defines the area"""
        return self.__width * self.__height

    def __str__(self):
        """print string representation"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
