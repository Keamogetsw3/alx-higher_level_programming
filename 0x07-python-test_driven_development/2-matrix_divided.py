#!/usr/bin/python3
"""Defines a function to perform scalar division on a matrix."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a scalar value.

    Args:
        matrix (list of lists): A matrix (list of lists) containing
            integers or floats.
        div (int or float): The scalar value by which to divide
            each matrix element.

    Returns:
        list of lists: A new matrix with the elements divided by `div`,
            rounded to two decimal places.

    Raises:
        TypeError: If `matrix` is not a list of lists of integers/floats.
        TypeError: If rows of `matrix` are not of equal size.
        TypeError: If `div` is not a number (integer or float).
        ZeroDivisionError: If `div` is zero.
    """
    import decimal

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(error_msg)

    len_rows = []
    row_count = 0

    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)
        len_rows.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error_msg)
        row_count += 1

    if len(set(len_rows)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if int(div) == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(
        map(lambda row: list(map(lambda x: round(x / div, 2), row)), matrix)
    )

    return new_matrix
