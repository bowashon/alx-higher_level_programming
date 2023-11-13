#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a class Square that inherits
    from the class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        defines class Square constructor
        with id, x, y, width and height
        the width and height are assigned to value size
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overloading __str__ method
        """
        return "[{}] ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.y,
                   self.width)

    @property
    def size(self):
        """
        retrieves the size of the rectangle
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Assigns the value for the width and height
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Public instantiation method
        that updates the class Square
        """
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.size = args[1] if len(args) >= 2 else self.size
            self.x = args[2] if len(args) >= 3 else self.x
            self.y = args[3] if len(args) >= 4 else self.y
        elif kwargs:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """
        return the dictionary representation of a Square
        """
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
               }
