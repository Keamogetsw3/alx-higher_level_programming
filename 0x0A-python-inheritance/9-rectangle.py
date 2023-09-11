#!/usr/bin/python3
"""
Defines the BaseGeometry class.
"""

class BaseGeometry:
    """ An empty class. """
    def area(self):
        """
        Raises an exception when called; needs to be implemented by subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the given `value` is an integer greater than 0.

        Args:
            name: The value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """
    A representation of a rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns an informal string representation of the rectangle.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
