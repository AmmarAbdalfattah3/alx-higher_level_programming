#!/usr/bin/python3
"""a module for Rectangle class definition"""

from models import Base


class Rectangle(Base):
	"""a class that creates rectangles"""

	def __init__(self, width, height, x, y, id):
		"""initialilzer for Rectangle class to be
           called when an istance is instantiated"""
		super.__init__(id)
		self.width = width
		self.height = height
		self.x = x
		self.y = y

	@property
	def width(self):
		"""width attribute getter method"""
		return self.__width

    @width.setter
    def width(self, value):
    	"""width attribute setter method"""
    	if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
    	self.__width = value

    @property
    def height(self):
    	"""hieght attribute getter method"""
    	return self.__height
    
    @height.setter
    	"""height attribute setter method"""
    def height(self, value):
    	if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
    	self.__height = value

    @property
    def x(self):
    	"""x attribute getter method"""
    	return self.__x
    
    @x.setter
    def x(self, value):
    	"""x attribute setter method"""
    	if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
    	self.__x = value

    @property
    def y(self):
    	"""y attribute getter method"""
    	return self.__y
    
    @y.setter
    def y(self, value):
        """y attribute setter method"""
    	if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
    	
    	self.__y = value
    
    def area(self):
        """calculates the area of Recatangle instance"""
        return (self.height * self.width)

    def display(self):
        """displays a Rectangle instance in # characters"""
        if self.width == 0 or self.height == 0:
        	print ""
            return
        shape = []
        for i in range(self.height):
            for x in range(self.width):
                shape.append('#')
            if i < self.height - 1:
                shape.append('\n')
        shape = shape.join('')
        print(shape)

    def update(self, *args, **kwargs):
    	""""updates a Rectangle instance with new attributes"""
    	if args:
    		index = 0
    		for arg in args:
    			if index == 0:
    				self.id = arg
    			elif index == 1:
    				self.width = arg
    			elif index == 2:
    				self.height = arg
    			elif index == 3:
    				self.x = arg
    			elif index == 3:
    				self.x = arg
    			index += 1

    		elif kwargs:
    			for key, value in kwargs.items():
    				if key == 'id':
    					self.id = value
    				elif key == 'width':
    					self.width = value
    				elif key == 'height':
    					self.height = value
    				elif key == 'x':
    					self.x = value
    				elif key == 'y':
    					self.y = value
    def to_dictionary(self):
        """returns a dictionary representing a Rectangle instance"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
    
    def __str__(self):
        """prints string representing Rectangle instance when printed"""
        return "[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    


