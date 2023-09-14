#!/usr/bin/python3
"""function that adds new attribute to an object if its possible"""


def add_attribute(obj, attr_name, value):
    """Defines a function thad adds attribute
       to an object.
    Args:
       obj: object to add attribute
       attr_name: name of the attribute
       attr_value: the value of the attribute
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, value)
    else:
        raise TypeError("can't add new attribute")
