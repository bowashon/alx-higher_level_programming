#!/usr/bin/python3
"""function tha reurns list of available attributes
   and methods of an object."""


def lookup(obj):
    """
    Args:
        obj: the object to inspect.

    Returns:
        A list of strings representing the attributes and methods of the obj
   """
    lists = []
    for attr in dir(obj):
        lists.append(attr)
    return lists
