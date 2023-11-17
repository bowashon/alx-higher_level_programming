#!/usr/bin/python3
""" Function that prints name: first name and last name"""


def say_my_name(first_name, last_name=""):
    """
    Definition: Defines funtion that prints name
    Args:
        first_name: String that represents the first name
        Last_name: String that represents the last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
