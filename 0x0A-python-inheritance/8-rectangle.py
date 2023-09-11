#!/usr/bin/python3
"""
Defines a class Reactangle that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    an empty class Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes an instance of class Rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
