#!/usr/bin/python3
""" Defines a Square class """


class Square:
    """ Defines a Square class """
    def __init__(self, size=0):
        """Initializes the square.

        Args:
            size (int): The size of a side of the square
        """
        self.size = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """ Getter for the size attribute

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """S etter for the size attribute

        Args:
            value (int): The size of a side of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
