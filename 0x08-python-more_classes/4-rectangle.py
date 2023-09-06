#!/usr/bin/python3
""" 
Define a class called Rectangle 
"""

class Rectangle:
    """
    Represent an empty class for creating rectangles
    """

    def __init__(self, width=0, height=0):
         """" 
        Initialise the instance
        
        Args:
            width: witdth of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter method for width property """
        return self.__width

    @property
    def height(self):
        """ Getter method for height property """
        return self.__height

    @width.setter
    def width(self, value):
        """ Setter method for width property """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ Setter method for height property """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ return the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ return the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """ Return a string to print the rectangle with '#' characters """
        if self.width == 0 or self.height == 0:
            return ''
        to_print = ''
        for col in range(self.height):
            for row in range(self.width):
                to_print += '#'
            if col != self.height - 1:
                to_print += '\n'
        return to_print

    def __repr__(self):
        """ Return a string representation of the rectangle """
        return 'Rectangle({}, {})'.format(self.width, self.height)
