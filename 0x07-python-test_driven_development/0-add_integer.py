#!/usr/bin/python3
"""Function that adds 2 integers"""


def add_integer(a, b=98):
    """ Defines a function that adds 2 integers

    Args:
        a: first integer to be added
        b: secod integer to be added, By default: b = 98

    return:
        return: the sum of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
