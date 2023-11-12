#!/usr/bin/python3
"""class Base module"""


class Base:
    """
    Definition:
        Defines a class Bass
    instantiation:
        instantiate with constructor
        def __init__(self, id=None):
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
