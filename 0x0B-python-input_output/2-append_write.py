#!/usr/bin/python3
'''
Defines a function to append a string to a text file.
'''


def append_to_file(filename="", text=""):
    '''
    Appends a string at the end of a text file (UTF8).
    Args:
       filename (str): The file to which text will be appended.
       text (str): The text to be appended.

       Returns:
       int: The number of characters appended.
    '''
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
