#!/usr/bin/python3
"""This module defines the class-to-json function."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure"""
    return obj.__dict__
