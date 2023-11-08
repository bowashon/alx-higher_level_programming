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

    def to_json(self):
        """
        public method that retrieves a dictionary
        representation of the student
        """
        return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
               }
