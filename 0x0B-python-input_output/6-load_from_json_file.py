#!/usr/bin/python3
"""load from json file module"""
import json


def load_from_json_file(filename):
    """function that creates an object
    from a "JSON file"
    """
    with open(filename, 'r', encoding="UTF8") as f:
        load_file = json.load(f)
        return (load_file)
