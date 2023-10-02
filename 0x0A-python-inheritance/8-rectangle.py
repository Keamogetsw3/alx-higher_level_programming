#!/usr/bin/python3
"""
    Module that provides information about the available attributes and methods of an object.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ 
    A class that represents a rectangle, inheriting from the BaseGeometry class.
    """

    def __init__(self, width, height):
        """ 
        Initializes an instance of the Rectangle class with width and height parameters.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
