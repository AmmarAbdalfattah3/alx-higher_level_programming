#!/usr/bin/python3
"""a module defining add_attribute fucntion"""


def add_attribute(obj, key, val):
    """Add a new attribute to an object if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[key] = val
