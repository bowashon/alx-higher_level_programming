#!/usr/bin/python3
"""Improve class BaseGeometry"""


class BaseGeometry:
    """Defines a class BaseGeometry"""

    def area(self):
        """Define an instance method area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Creates a public instance method
        Args:
        name: string that defines the name
        value: set the name value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = value
