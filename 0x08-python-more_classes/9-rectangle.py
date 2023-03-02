#!/usr/bin/python3
"""Rectangle class definition module"""


class Rectangle:
    """class definition of a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializer of Rectangle class"""
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Instance property width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Instance property width setter"""
        if type(width) is not int:
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
        if type(width) is not int:
            raise TypeError('with must be an integer')
        if width < 0:
            raise ValueError('with must be >= 0')
        self.__width = value

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

    def __str__(self):
        """ prints the width and height of
            a Rectangle class instance usig
            # characters
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rec_form = []
        for i in range(self.__height):
            for x in range(self.__width):
                rec_form.append(str(self.print_symbol))
            if i < self.__height - 1:
                rec_form.append('\n')
        return rec_form.join('')

    def __repr__(self):
        """returns a string representation of any Rectangle instance"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """prints a good by message when an instance is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the rectangle with the bigger area"""
        if type(rect_1) not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with
           width, height and size are equal.
        """
        return (cls(size, size))
