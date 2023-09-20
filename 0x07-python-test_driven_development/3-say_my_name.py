#!/usr/bin/python3
"""Function that prints name"""


def say_my_name(first_name, last_name=""):
    """
    Definition: define a function that prints first name and last name

    Args:
        first_name: the first name
        last_name: last name
    Return:
        Return the string "My name is <first name> <last name>
    """
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
