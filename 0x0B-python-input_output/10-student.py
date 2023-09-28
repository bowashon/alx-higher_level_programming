#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """
    Definition:
        Defines a class student by public intances
        first_name, last_name, age
    """

    def __init__(self, first_name, last_name, age):
        """initialize instance self
           first_name, last_name, age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        filtered_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                filtered_dict[key] = value
        return filtered_dict
