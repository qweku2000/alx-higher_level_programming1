#!/usr/bin/python3

from models.base import Base

"""Define a rectangle class"""
class Rectangle(Base):
    """Represent a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize new rectangle
        Arguments:
        width(int) the width 
        height(int) the height
        x(int) the x coordinate 
        y(int) the y coordinate

        raises:
        TypeError: If width or height is not an int.
        ValueError: If of width or height <= 0.
        TypeError: If of x or y is not an int.
        ValueError: If of x or y < 0.  
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    @property
    """Set/get width"""
    def width(self):
        return self.__width

    @width.setter
    def width(self,val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0 :
            raise ValueError("width must be > 0")
        self.__width = val
    
    @property
    def height(self):
        return self.__height

    
    @height.setter
    """Set/get height"""
    def height(self,val):
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <=0 :
            raise ValueError("height must be > 0")
        self.__height = val
    
    @property
    """ set/get x coordinate """
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,val):
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")

    @property
    """set/get the y coordinate"""
    def y(self):
        return self.__y

    @y.setter
    def y(self,val):
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
