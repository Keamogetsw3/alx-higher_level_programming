#!/usr/bin/python3
""" This module defines a MagicClass that can be used for various calculations related to circles, such as calculating the area and circumference
"""

import math

class MagicClass:
    """Initialization of the MagicClass."""
    def __init__(self, radius=0):
        """Initialize the MagicClass with an optional radius.

        Args:
            radius (float): The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If the provided radius is not a number.
        """
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
