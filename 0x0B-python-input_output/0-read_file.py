#!/usr/bin/python3
"""
Defines a function to read and print the contents of a file.
"""

def read_file(filename=""):
    """
    Reads a file and prints its content.

    Args:
        filename (str): The name of the file to be read. Defaults to an empty string.
    """

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
