#!/usr/bin/python3
"""
Define a Base model class
"""
import jsn
import csv
import turtle


class Base:
    """ 
    This class will be the “base” of all other classes in this projec
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int): The ID for the object. If not provided, it will be automatically generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
