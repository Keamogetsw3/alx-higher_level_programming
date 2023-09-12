#!/usr/bin/python3
"""
Defines a function that creates an Object from a “JSON file”.
"""
import json


def load_from_json_file(filename):
    """
    Loads JSON data from a specified file.

    Args:
        filename (str): The path to the JSON file to load.

    Returns:
        object: The Python object created from the JSON data in the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
