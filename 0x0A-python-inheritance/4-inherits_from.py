#!/usr/bin/python3
"""
Module for inherits_from
"""


def inherits_from(obj, a_class):
    """
    Checks if the given object is an instance of a class that has inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to be checked for inheritance.

    Returns:
        True if obj is an instance of a class that inherited from a_class, otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
