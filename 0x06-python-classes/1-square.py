#!/usr/bin/python3
"""defining a square class"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of a side of the square

    """
    def __init__(self, size_square):
        """Initializes a square

        Args:
            size_square (int): size of a side of the square

        """
        self.__size = size_square
