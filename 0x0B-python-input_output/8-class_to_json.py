#!/usr/bin/python3
"""
Defines a function for converting a class instance to a JSON-like dictionary.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure.
    Args:
        obj (object): The object to be converted into a dictionary.

    Returns:
         dict: A dictionary representation of the input object's attributes.
    """
    return obj.__dict_
