#!/usr/bin/python3
import json
"""from json string to objec"""


def from_json_string(my_str):
    """
    Returns:
    returns the object represented bj
    JSON string
    """
    return (json.loads(my_str))
