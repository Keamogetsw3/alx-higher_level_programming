#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for column in row:
                print("{:d}".format(column), end=" ")
            print()
