#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    def square_value(value):
        return value**2

    squared_matrix = [list(map(square_value, row)) for row in matrix]

    return squared_matrix
