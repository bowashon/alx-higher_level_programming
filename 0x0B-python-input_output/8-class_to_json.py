#!/usr/bin/python3
""" Return dictionary description module"""


def class_to_json(obj):
    """
    returns the dictionary description fo
    a JSON serialization of an object
    """
    return obj.__dict__
