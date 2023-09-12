#!/usr/bin/python3
"""
Defines a function for converting a Python object into a JSON string."""
import json


def to_json_string(my_obj):
    """
    Converts a Python object into a JSON string.

    Args:
        my_obj (any): The Python object to be converted to JSON.

    Returns:
        str: A JSON string representation of the input object.
    """
    return json.dumps(my_obj)
