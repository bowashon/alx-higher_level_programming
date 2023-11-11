#!/usr/bin/python3
""" class Student module"""


class Student:
    """
    Defines a class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        instantiate:
        first_name: student's first name
        last_name: student's last name
        age: studentst age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        public method that retrieves a dictionary
        representation of the student
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__

        my_dict = {}
        for attr in attrs:
            if not isinstance(attr, str):
                return self.__dict__

        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict

    def reload_from_json(self, json):
        """
        public method that replaces all attributes of
        the Student instance
        """
        if json is None or not isinstance(json, dict):
            return self.__dict__

        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
