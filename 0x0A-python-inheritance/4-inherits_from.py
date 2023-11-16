#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an istance of the
    class that inherited (directly or indirectly) from
    a specified class; otherwise False
    """
    return ( isinstance(obj, a_class) and type(obj) != a_class)
