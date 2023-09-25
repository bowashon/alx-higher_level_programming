#!/usr/bin/python3
"""function that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    Definition:
        Defines a function that returns an obj represented by JSON string
    Args:
        my_str: JSON string
    """

    return json.loads(my_str)
