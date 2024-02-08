#!/usr/bin/python3

"""
A class Rectangle that defines a rectangle
width must be an integer, width need to be less than 0
height must be an integer, height need to be less than 0
"""


class Rectangle:
    """
    A class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def my_print(self):
        print("{}{}".format(self.__height, self.__width))

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height + self.__width) * 2)
