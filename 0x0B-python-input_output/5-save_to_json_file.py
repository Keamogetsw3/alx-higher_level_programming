#!/usr/bin/python3
"""
Defines a function to save data to a file in JSON format.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save data to a file in JSON format or create the file if it doesn't exist.

    Args:
        my_obj: The Python object to be saved as JSON.
        filename (str): The name of the file to save the JSON data to.
    """
    with open(filename, mode="w", encoding="utf-8") as _file:
        _file.write(json.dumps(my_obj))
