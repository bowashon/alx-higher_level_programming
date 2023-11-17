#!/usr/bin/python3
"""Function that divides a matrix"""


def matrix_divided(matrix, div):
    """
    Definition: function that divides a matrix
    Args:
        matrix: the matrix to be divided
        div: the divisor
    Return:
        Returns the result of the divided matrix
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_mat = []

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []

        for element in row:
            if not isinstance(element, (int, float)):
                raise ValueError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")
            new_row.append(round(element / div, 2))
        new_mat.append(new_row)

    return new_mat
