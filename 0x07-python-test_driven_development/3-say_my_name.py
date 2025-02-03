#!/usr/bin/python3
"""
This module provides a function to print a person's full name.

The `say_my_name` function takes a first name and an optional last name 
and prints a formatted message.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name to be printed.
        last_name (str, optional): The last name to be printed. Defaults to an 
            empty string.

    Raises:
        TypeError: If `first_name` or `last_name` is not a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)
