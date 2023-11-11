#!/bin/usr/python3
"""The append after module"""


def append_after(filename="", search_string="", new_string=""):
    """
    Definition:
         Defines function that append new string
         After a search string is found
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w', encoding="UTF8") as new_file:
        for line in lines:
            new_file.write(line)
            if search_string in line:
                new_file.write(new_string)
