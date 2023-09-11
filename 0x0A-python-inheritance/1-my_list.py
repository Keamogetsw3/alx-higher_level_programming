#!/usr/bin/python3
""" 
Defines a class Mylist that inherits from 'list'
"""


class MyList(list):
    """ 
    Define a method to print the list elements in sorted order.
    """

    def print_sorted(self):
        """ Sort the list in ascending order and print """
        print(sorted(self))
