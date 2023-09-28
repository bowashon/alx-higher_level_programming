#!/usr/bin/python3
"""Function that returns lists of integers
   representing the Pascal's triangle
"""


def pascal_triangle(n):
    """
    Definition:
        Defines a the returns a lists of integers
        representing the Pascals's triangle
    Args:
        n: the number of integers to be returned
    Return:
        returns a lists of integers representing the
        Pascal's triange
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            row.append(1)
        triangle.append(row)
    return triangle
