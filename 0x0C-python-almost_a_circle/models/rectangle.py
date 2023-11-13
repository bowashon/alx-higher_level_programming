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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retieves the heights"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieves the x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieves the y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """public method that returns area
        of the rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
        prints to the stdout the Rectangle instance
        with the character #
        """
        print('\n' * self.__y + (' ' * self.__x + '#' * self.__width + '\n') *
              self.__height, end='')

    def __str__(self):
        """
        return string representation
        """
        return "[{}] ({}) {}/{} - {}/{}".\
            format(type(self).__name__, self.id, self.__x, self.__y,
                   self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        update the class Rectangle by adding public
        method that assigns an argument to each
        attribute
        """
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.width = args[1] if len(args) >= 2 else self.width
            self.height = args[2] if len(args) >= 3 else self.height
            self.x = args[3] if len(args) >= 4 else self.x
            self.y = args[4] if len(args) >= 5 else self.y
        elif kwargs:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.y = kwargs.get('y', self.x)
            self.x = kwargs.get('x', self.x)

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
               }
