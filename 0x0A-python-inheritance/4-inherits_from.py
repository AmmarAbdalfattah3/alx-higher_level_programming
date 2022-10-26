#!/usr/bin/python3
"""This module contains the inherits_from function"""


def inherits_from(obj, a_class):
    """Return True or False"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
