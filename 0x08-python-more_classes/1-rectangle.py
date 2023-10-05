#!/usr/bin/python3
class Rectangle:
    def __init__(self,width=0,height=0):
        if type(width)is not int:
            raise TypeError("width must be an integer")
        if width < 0 :
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must >= 0")
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width
    @width.getter
    def width(self,value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0 :
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        return self.__height

    def height(self,value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must >= 0")
        self.__height = value
        
