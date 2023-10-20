#!/usr/bin/python3
"""Defines a Rectangle class"""
from models.base import Base

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
    def width(self):
        """Set/get width"""
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
        """Set/get height"""
        return self.__height

    
    @height.setter
    def height(self,val):
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <=0 :
            raise ValueError("height must be > 0")
        self.__height = val
    
    @property
    def x(self):
        """Set/get x coordinate"""
        return self.__x
    
    @x.setter
    def x(self,val):
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """Set/get y coordinate"""
        return self.__y

    @y.setter
    def y(self,val):
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
    
    def area(self):
        """Returns the area of rectangle instance"""
        return self.height * self.width

    def display(self):
        """Print rectangle with # character."""
        for i in range(self.height):
                for j in  range(self.width):
                    print("#",end="")
                print()

    def __str__(self):
         return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"


    def update(self, *args):
        """
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
