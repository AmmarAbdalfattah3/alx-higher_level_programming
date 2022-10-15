#!/usr/bin/python3
"""this module contains 0-add_integer.py"""

def add_integer(a, b=98):
    """ return the addition of a and b

       Args:
           a (int): the first integer to be added
           b (int): the second integer to be added

    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
