#!/usr/bin/python3
""" 
Module for is_same_class 
"""


def is_same_class(obj, a_class):
    """
    Check if the given object is exactly an instance of the specified class.

    Args:
    obj: Any object to be checked.
    a_class: The class to compare against.

    Returns:
    True if obj is exactly an instance of a_class, otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False
