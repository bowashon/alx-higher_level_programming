#!/usr/bin/python3
""" function that writes an Object to a text file """
import json


def save_to_json_file(my_obj, filename):
    """
    Definition:
        Defines a function that object to a text file
    Args:
        my_obj: the obj file
        filename: name of the file
    """

    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
