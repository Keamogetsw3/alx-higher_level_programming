#!/usr/bin/python3
"""
Defines a function which splits text into lines
"""

def text_indentation(text):
    """
    Splits a text into lines along "?", ":", and "." followed by two new lines.
    
    Args:
        text (str): The input text to be processed.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    flag = 0
    
    for char in text:
        if flag == 0:
            if char == ' ':
                continue
            else:
                flag = 1
        
        if flag == 1:
            if char in ['?', '.', ':']:
                print(char)
                print()
                flag = 0
            else:
                print(char, end="")
