#!/usr/bin/python3
"""

A python unittest for class rectangle

"""


import unittest, sys, io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_rectangle(unittest.TestCase):
    """
    Class for unittest rectangle
    """
    def test_construtor(self):
        """Test init of Rectangle class"""
        r = Rectangle(5, 10, 1, 2, 3)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 3)

    def test_area(self):
        """Test the area metohd of Rectangle class"""
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), (50))

    def test_display(self):
        """Test the display method of the Rectangle class"""
        r = Rectangle(2, 3)
        original_stdout = sys.stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = original_stdout
        self.assertEqual(captured_output.getvalue(), "##\n##\n##\n")

    def test_str(self):
        """Test the str method of Rectangle class"""
        r = Rectangle(5, 10, 1, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (3) 1/2 - 5/10")

    def test_update(self):
        """Test the update method of Rectangle class"""
        r = Rectangle(5, 10, 1, 2, 3)
        r.update(4, 6, 11, 2, 3)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 11)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_to_dictionary(self):
        """Test the to_dictonary methode of Rectangle class"""
        r = Rectangle(5, 10, 1, 2, 3)
        d = {'x': 1, 'y': 2, 'id': 3, 'height': 10, 'width': 5}
        self.assertEqual(r.to_dictionary(), d)
