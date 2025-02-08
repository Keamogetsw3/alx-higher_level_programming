#!/usr/bin/python3
""" This module defines the Square class """


class Square:
    """ Represents a square object with a specified size
    """
    def __init__(self, size=0):
        """ Initializes a Square instance with a given size

        Args:
            size (int): The size of the square """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """ Getter for the size property

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for the size property

        Args:
            value (int): The size of the square

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If the input is negative
        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ Calculate the area of the square

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __le__(self, other):
        """ Check if this square is less than or equal to another square

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square is less than or equal to the other square, False otherwise.
        """
        return self.area() <= other.area()

    def __lt__(self, other):
        """ Check if this square is less than another square

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square is less than the other square, False otherwise.
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """ Check if this square is equal to another square

        Args:
            other (Square): The other square to compare

        Returns:
            bool: True if this square is equal to the other square, False otherwise
        """
        return self.area() == other.area()

    def __ge__(self, other):
        """ Check if this square is greater than or equal to another square

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square is greater than or equal to the other square, False otherwise.
        """
        return self.area() >= other.area()

    def __gt__(self, other):
        """
        Check if this square is greater than another square

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square is greater than the other square, False otherwise.
        """
        return self.area() > other.area()

    def __ne__(self, other):
        """
        Check if this square is not equal to another square

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square is not equal to the other square, False otherwise.
        """
        return self.area() != other.area()
