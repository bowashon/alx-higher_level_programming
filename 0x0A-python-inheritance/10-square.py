#!/usr/bin/python3
""" class square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines class Square that inherits from
    Rectangle
    """

    def __init__(self, size):
        """
        Instantiation with size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calculate the area"""
        return self.__size ** 2

    def __str__(self):
        """string representation of the square"""
        return ("[{}] {}/{}".format(self.__class.__name__, self.__size,
                self.__size))
