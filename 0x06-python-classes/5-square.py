#!/usr/bin/python3
"""defining a square class"""


class Square:
    """Represents a square class

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes a square

        Args:
            size (int): size of a side of the square

        """
        self.size = size

    @property
    def size(self):
        """`__size getter

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ the setter of the size attribute

        Args:
            value (int): the size of the square

        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):


        """calculates area of the square
        Returns:
            The square's area
        """
        return (self.__size) ** 2

    def my_print(self):
        """prints in stdout"""

        for x in range(self.__size):
            for n in range(self.__size):
                print("#", end="")
        print("")
        if (self.__size == 0):
            print("")
