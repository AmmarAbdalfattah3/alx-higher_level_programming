#!/usr/bin/python3
"""defining a square class"""


class Square:
    """Represents a square class

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square

        Args:
            size (int): size of a side of the square

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """__position getter

        Returns:
            The position of the square

        """
        return self.__position

    @position.setter
    def position(self, value):
        """ the setter of the position attribute

        Args:
            value (int): the position of the square

        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    def area(self):
        """calculates area of the square

        Returns:
            The square's area

        """
        return (self.__size) ** 2

    def my_print(self):
        """prints in stdout"""

        for x in range(self.__position[1]):
            print("")
        for n in range(self.__size):
            print("".join([" " for i in range(self.__position[0])]), end="")
            print("".join(["#" for m in range(self.__size)]))

        if (self.__size == 0):
            print("")
