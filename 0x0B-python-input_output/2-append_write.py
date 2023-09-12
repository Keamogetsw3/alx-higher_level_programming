#!/usr/bin/python3
"""
Defines function that appends a string at the end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)