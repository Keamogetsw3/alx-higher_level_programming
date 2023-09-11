#!/usr/bin/python3
"""
Module for is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if it inherits from, the specified class.

    Args:
    obj: The object to be checked.
    a_class: The class to check against.

    Returns:
    True if obj is an instance of a_class or a subclass of a_class, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
