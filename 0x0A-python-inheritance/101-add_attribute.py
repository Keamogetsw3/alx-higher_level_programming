#!/usr/bin/python3
"""
Module: attribute_adder

This module efines a function that adds attributes to objects.
"""


def can_add_attribute(obj, name, value):
    """
    Adds new attribute to an object if possible

    Args:
        obj (any): The object to add an attr
        name (str)): The name of attribute to add o obj
        value (any): The value of the attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("Can't add new attribute")
    setattr(obj, name, value)
