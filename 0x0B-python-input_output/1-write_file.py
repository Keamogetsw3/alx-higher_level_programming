#!/usr/bin/python3
"""
Defines the function  that writes a string to a text file (UTF8).
"""


def write_file(filename="", text=""):
    """
    Writes text' to file and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
