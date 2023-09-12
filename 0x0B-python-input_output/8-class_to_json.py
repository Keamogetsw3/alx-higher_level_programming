#!/usr/bin/python3
"""
Defines a Python function for converting a class instance to a JSON-like dictionary.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.
    
    Args:
        obj (object): The object to be converted into a dictionary.

    Returns:
         dict: A dictionary representation of the input object's attributes.
    """
    return obj.__dict_
