#!/usr/bin/python3
"""
Defines a function that returns an object (Python data structure) represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Converts a JSON string to its Python object representation.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python object representation of the JSON string.
    """
    return json.loads(my_str)
