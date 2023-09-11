#!/usr/bin/python3
"""
Finding a list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Takes an object as input and returns a list of its available attributes and methods.

    Args:
        obj: Any Python object.

    Returns:
        list: A list of strings containing the names of attributes and methods of the object.
    """
    return dir(obj)
