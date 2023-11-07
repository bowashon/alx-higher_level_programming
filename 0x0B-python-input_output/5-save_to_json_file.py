#!/usr/bin/python3
"""write object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an object to a text file,
    using JSON representation
    """
    with open(filename, 'w', encoding="UTF8") as f:
        json.dump(my_obj, f)
