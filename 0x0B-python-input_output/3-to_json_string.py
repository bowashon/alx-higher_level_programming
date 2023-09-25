#!/usr/bin/python3
""" function that returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """
    Definition:
        Defines a function that returns the json representation of object
    Args:
        my_obj: the object file
    Return:
        Returns the json representation of an object file
    """

    return json.dumps(my_obj)
