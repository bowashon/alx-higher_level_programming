#!/usr/bin/python3
"""class Base module"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes JSON string representation of
        lsit_objs to a file
        """
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), 'w') as f:
            f.write(cls.to_json_string(list_objs))
