#!/usr/bin/python3
"""The locked class module"""


class LokedClass:
    """
    Defines a class Locked classs with no class or object
    attribute, that prevents the user from dynamically
    creating new instance attribute, except if the new
    instance attribute is called first_name
    """
    __slots__ = ("first_name")
