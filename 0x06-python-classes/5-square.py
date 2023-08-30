#!/usr/bin/python3
""" Defines a Square class"""


class Square:
    """ Defines a Square class"""
    def __init__(self, size=0):
        """ Initializes a square object.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """ Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square.

        Args:
            value (int): The size of the square (must be an integer >= 0)
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square to stdout using the '#' character.
        """
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
