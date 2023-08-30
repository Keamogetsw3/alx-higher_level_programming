#!/usr/bin/python3
""" Defines a class MagicClass """
import math


class MagicClass:
    """ Defines a class MagicClass """
    def __init__(self, radius=0):
        """Initializes the Magic Class
        
        Arg:
            radius (float or int): The radius of the new MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculaes the area of the circle"""
        return (self.__radius ** 2) * math.pi
        
         def circumference(self):
             """Return circumference"""
              return 2 * math.pi * self.__radius
