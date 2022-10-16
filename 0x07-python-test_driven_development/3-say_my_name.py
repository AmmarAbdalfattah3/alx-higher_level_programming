#!/usr/bin/python3
k"""this module contains the say_my_name function"""
def say_my_name(first_name, last_name=""):
    """ return a new matrix

      Args:
          first_name (str): the first name
          last_name (str): the last name

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
