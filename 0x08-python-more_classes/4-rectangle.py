#!/usr/bin/python3
"""
Define a class called Rectangle
"""


class Rectangle:
    """ Represent an empty class for creating rectangles """

    def __init__(self, width=0, height=0):
        """" 
        Initialise the instance
        
        Args:
            width: witdth of the rectangle
            height: height of the rectangle
        """

    @property
    def width(self):
        """
        Returns the value of the width of the triangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ 
        Defines the width of the rectangle 

        args:
           value: the width
 
        Raise:
           
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value


    @property
    def height(self):
        """ Returns the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ 
        Defines height of the rectangle 
        
        args:
            value: height
            
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = ""
            for _ in range(self.__height):
                rectangle_str += "#" * self.__width + "\n"
            return rectangle_str[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)"
        
