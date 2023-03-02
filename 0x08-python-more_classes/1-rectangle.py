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
        if not isinstance(width, int):
            raise TypeError('with must be an integer')
        if width < 0:
            raise ValueError('with must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Instance property height getter"""
        return self.__width

    @height.setter
    def height(self, value):
        """Instance property height setter"""
        if not isinstance(width, int):
            raise TypeError('with must be an integer')
        if width < 0:
            raise ValueError('with must be >= 0')
        self.__width = value
