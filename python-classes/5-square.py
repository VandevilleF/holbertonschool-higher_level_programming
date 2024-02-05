#!/usr/bin/python3
"""
A class that defines a 'square'
"""


class Square:
    """
    A class named 'Square'
    """
    def __init__(self, size=0):

        if not type(size) is int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):

        if self.size == 0:
            print()
            return

        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
