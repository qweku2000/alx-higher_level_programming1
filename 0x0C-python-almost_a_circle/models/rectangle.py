#!/usr/bin/python3

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @width.setter
    def width(self,value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @width.getter
    def width(self):
        return self.__width

    @height.setter
    def heigt(self,value):
        if type(value) is not int:
            raise TypeError("Height must be integer")
        if value <= 0:
            raise ValueError("Height must be > 0 ")
        self.__height = value

    def height(self):
        return self.__height

    @x.setter
    def x(self,value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if x <= 0 :
            raise TypeError("x must be >= 0")
        self__x = value

    @x.setter
    def x(self):
        return self.__x

    @y.setter
    def y(self,value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if y <= 0:
            raise ValueError("y must be >= 0")
