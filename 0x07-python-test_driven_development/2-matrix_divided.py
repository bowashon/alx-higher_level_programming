#!/usr/bin/python3
"""Function that divides all element in a matrix"""


def matrix_divided(matrix, div):
    """Function that divides all element of a matrix
    Args:
        matrix: matrix with element
        div: divisor

    return: returns a new matrix divided by div and in two decimal places

    """
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(elem, (int, float)) for row in matrix for
                    elem in row)):
        raise TypeError("matrix must be a matrix (list of lists) of" +
                        " integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
