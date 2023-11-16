#!/usr/bin/python3
"""is_kind_of_class Module"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of
    or if the object is an istance of a class that
    inherited from a specific class
    """
    return (isinstance(obj, a_class))
