#!/usr/bin/python3
"""

A class Square that inherits from Rectangle

"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """def in str format for print"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(\
            self.id, self.x, self.y, self.width))
