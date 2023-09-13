#!/usr/bin/python3
"""class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    instantiation: defines class rectangle that inherite from
    base geometry
    """
    def __init__(self, width, height):
        """
	instantiation:
	Args:
	-----
	width: defines the width of the rectangle
	height: defines the height of the rectangle
	"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
