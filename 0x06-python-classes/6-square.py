#!/usr/bin/python3
"""Create Square class"""


class Square:
    """Define the class"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize class"""

        """Args:
        size (int)
        position
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an intefer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieve the position"""
        return self.__position

    @position.setter
    def position(self):
        """Defines or set position values."""
        if (not isinstance(value, turple)) or \
            len(value) != 2 or \
            not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with 'H' character."""
        if self.__size == 0:
            print(" ")
            return
    [print(" ") for i in range(0, self._position[0])]
    else:
        for _ in range(self.__position)
        [print(" ", end="")]
        for _ in range(self.__size):
            [print("#" * self.__size, end="")]
