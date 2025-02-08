#!/usr/bin/python3
def no_c(my_string):
    updated_str = []
    for char in my_string:
        if char != 'c' and char != 'C':
            updated_str.append(char)
    return ''.join(updated_str)
