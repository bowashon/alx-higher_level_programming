#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for row in matrix:
        print(" ".join("{:d}".format(element) for element in row))
