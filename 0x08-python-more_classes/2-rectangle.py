#!/usr/bin/python3
"""Rectangle class definition module"""


class Rectangle:
    """class definition of a rectangle"""

    def __init__(self, width=0, height=0):
        """initializer of Rectangle class"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Instance property width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Instance property width setter"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Instance property height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Instance property height setter"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ calculates rectangle area"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * self.__width

    def perimeter(self):
        """claculates rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
