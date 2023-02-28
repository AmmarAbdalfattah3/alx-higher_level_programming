#!/usr/bin/python3
"""This module prints a square with the character #"""


def print_square(size):
    """This function prints a square with the character #
    Args:
        size (int): is the size length of the square
    Raises:
        TypeError: If size is not an integer
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        for i in range(size):
            print("#", end="")
        print()
