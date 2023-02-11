#!/usr/bin/python3
"""MyInt class module"""


class MyInt(int):
    """a child of int class that changes != into == and vice versa"""

    def __eq__(self, val):
        """changes == into !="""
        return self.real != val

    def __ne__(self, val):
        """changes != int =="""
        return self.real == val
