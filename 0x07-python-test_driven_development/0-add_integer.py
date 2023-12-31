#!/usr/bin/python3
"""
Defines a function for integer addition.
"""


def add_integer(a, b=98):
    """
    Returns the result of adding two numbers as integers.

    Args:
        a: The first number.
        b: The second number. Defaults to 98.

    Returns:
        The result of adding 'a' and 'b' as integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")
    return int(a) + int(b)
