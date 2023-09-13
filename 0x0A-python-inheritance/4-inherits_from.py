#!/usr/bin/python3
"""check if object is an instance of a class
   that inherited (directly or indirectly)
"""


def inherits_from(obj, a_class):
    """
    check if object is instance of a class that inherited

    Args:
        obj: the object to check
        a_class: the class to compare
    Return: returns true or false
    """
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
