#!/usr/bin/python3
"""a module for Square class definition"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """a class that creates squres"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialilzer for Rectangle class to be
           called when an istance is instantiated
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size attribute getter method"""
        return self._size

    @size.setter
    def size(self, value):
        """size attribute setter method"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """"updates a Square instance with new attributes"""
        if args:
            index = 0
            for arg in args:
                if index == 1:
                    self.id = arg
                elif index == 2:
                    self.size(arg)
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg
                index += 1
        elif kwargs:
            for key, value in kwargs.items():
                if k == "id":
                    self.id = value
                elif k == "size":
                    self.size(value)
                elif k == "x":
                    self.x = value
                elif k == "y":
                    self.y = value

    def to_dictionary(self):
        """returns a dictionary representing a Square instance"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

        def __str__(self):
            """prints string representing Square instance when printed"""
            return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
