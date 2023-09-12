#!/usr/bin/python3
""" function that checks if an object is
    an instance of a specified class
"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class"""
    if type(obj) == a_class:
        return True
    else:
        return False
