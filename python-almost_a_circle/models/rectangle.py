#!/usr/bin/python3
"""

Class Rectangle inherits from Base

"""


from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Init Rectangle with a given width, height, x and y"""
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @property
    def x(self):
        """Get the x of the rectangle"""
        return self.__x

    @property
    def y(self):
        """Get the y of the rectangle"""
        return self.__y

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set the x of the rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set the y of the rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays a representation of the rectangle"""
        for row in range(self.__height):
            for line in range(self.__width):
                print("#",end="")
            print()

    def __str__(self):
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(\
            self.id, self.__x, self.__y, self.__width, self.__height))
