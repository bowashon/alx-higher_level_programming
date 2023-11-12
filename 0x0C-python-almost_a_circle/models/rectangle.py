#!/usr/bin/python3
"""class Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """
    Defines class rectangle that inherits
    from a Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """return the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        self.__width = value

    @property
    def height(self):
        """retieves the heights"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value of the height"""
        self.__height = value

    @property
    def x(self):
        """retrieves the x value"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """retrieves the y value"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
