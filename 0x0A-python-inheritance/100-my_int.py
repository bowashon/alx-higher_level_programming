#!/usr/bin/python3
"""Class Myint that inherits from int"""


class MyInt(int):
    """Defines class MyInt"""
    def __eq__(self, other):
        """To invert the equal method"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """To invert the not equal method"""
        return not super().__ne__(other)
