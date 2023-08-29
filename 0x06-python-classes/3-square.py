#!/usr/bin/python3
""" Defines a class Square"""


class Square:
    """ Defines a class Square"""

    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
         """returns the current square area"""
        return self.__size * self.__size
