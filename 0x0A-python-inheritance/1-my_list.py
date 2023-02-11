#!/usr/bin/python3
"""A module for Mylist class"""


class MyList(list):
    """a child of List class"""

    def __init__(self):
        """initializes the class instance"""
        super().__init__()

    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
