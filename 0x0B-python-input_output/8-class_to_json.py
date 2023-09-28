#!/usr/bin/python3
"""function that returns dictionary description"""


def class_to_json(obj):
    """
    Definition:
        Defines function that returns dictionary description
    Arg:
       obj: object for JSON serialization
    Return:
        Returns dictionary description with simple data structure
    """
    return obj.__dict__
