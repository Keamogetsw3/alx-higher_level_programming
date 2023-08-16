#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix is None:
        matrix = []

    new_matrix = []
    for row in matrix:
        new_row = list(map(lambda num: num ** 2, row))
        new_matrix.append(new_row)
    return new_matrix
