#!/usr/bin/python3
""" A class that defines a square"""


class Square:
    """Defines a square Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiate the Square

        Args:
        size: This declares the size of the square.
        position: This indicate the position of print
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieves the value"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    @property
    def position(self):
        """To retrieve it"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the value"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__positon = value

    def area(self):
        """Defines the area of the Square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints to stdout the square"""
        if self.__size == 0:
            print("")
            return

            [print("") for _ in range(0, self.___position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for _ in range(0, self.__position[0])]
            [print("#", end="") for _ in range(0, self.__size)]
            print("")

    def __str__(self):
        """prints the string representation of the square"""
        if self.__size != 0:
            [print("") for _ in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for _ in range(0, self.__position[0])]
            [print("#", end="") for _ in range(0, self.__size)]
            print("")
        return ("")
