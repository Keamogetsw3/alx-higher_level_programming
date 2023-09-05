#!/usr/bin/python3
"""
Defines a single function that prints a squaree
"""


def print_square(size):
    """
    Prints a square made of "#" characters with each side having a length equal to 'size'.

    args:
        size (param): An integer specifying the length of each side of the square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
