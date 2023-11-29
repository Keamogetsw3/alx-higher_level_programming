#!/usr/bin/python3
"""
Define a class called Rectangle
"""


class Rectangle:
    """ Represent an empty class for creating rectangles """
    def __init__(self, width=0, height=0):
        """ 
            Initialize the Rectangle with optional width and height arguments

            args:
                width:
                height:
            """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ 
            method for returning the width attribute
            
            Returns:
                    width of the rectangle
                    
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            method that defines the width attribute
            
            args:
                value:
        """
        if not isinstance(value, int):
            """ Check if the provided value is an integer, raise an error if not
            """
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter method for the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for the height attribute
        
            args:
                value:
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
