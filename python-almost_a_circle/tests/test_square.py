#!/usr/bin/python3
"""

A python unittest for class square

"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_square(unittest.TestCase):
    """
    Class for unittest square
    """
    def setUp(self):
        """Initialize square instance"""
        self.square = Square(5)

    def tearDown(self):
        """Delete square instance"""
        del self.square

    def test_square_inherits_from_base(self):
        """ Testing inheritance """
        self.assertTrue(issubclass(Square, Base))

    def test_attributes(self):
        """Check the initial attributes of the Square instance"""
        self.assertEqual(self.square.width, 5)
        self.assertEqual(self.square.height, 5)
        self.assertEqual(self.square.x, 0)
        self.assertEqual(self.square.y, 0)

    def test_size_setter(self):
        """Check the size setter method of the Square"""
        with self.assertRaises(TypeError):
            self.square.size = "invalid"
        with self.assertRaises(ValueError):
            self.square.size = 0

    def test_string_representation(self):
        """Check the string representation of the Square instance"""
        expected_output = "[Square] (9) 0/0 - 5"
        self.assertEqual(str(self.square), expected_output)

    def test_update_method(self):
        """Check the update method of the Square"""
        self.square.update(1, 10, 10, 10)
        self.assertEqual(self.square.id, 1)
        self.assertEqual(self.square.size, 10)
        self.assertEqual(self.square.x, 10)
        self.assertEqual(self.square.y, 10)

        self.square.update(size=15, y=5)
        self.assertEqual(self.square.size, 15)
        self.assertEqual(self.square.y, 5)

    def test_to_dictionary_method(self):
        """Check the to_dictionary method of the Square"""
        expected_dict = {'id': 10, 'x': 0, 'size': 5, 'y': 0}
        self.assertEqual(self.square.to_dictionary(), expected_dict)
