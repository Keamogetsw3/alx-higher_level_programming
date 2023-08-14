#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            print("".join("{:d}".format(column), end=" "))

        else:
            print()
