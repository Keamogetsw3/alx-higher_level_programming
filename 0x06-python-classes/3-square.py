#!/usr/bin/python3
""" Defines a class Square"""


class Square:
    """ Defines a class Square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
       """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """calculates the square area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2
