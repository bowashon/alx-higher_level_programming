#!/usr/bin/python3
"""function that creates an Object from a "JSON file"""
import json


def load_from_json_file(filename):
    """
    Definition:
        function that creates an object from a JSON file
     Args:
         filename: name of json file
     """

    with open(filename, "r") as f:
        return json.loads(f.read())
