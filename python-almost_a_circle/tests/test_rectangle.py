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

    def test_update_args(self):
        """Test the update method of Rectangle class"""
        r = Rectangle(5, 10, 1, 2, 3)
        r.update(4, 6, 11, 2, 3)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 11)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_update_kwargs(self):
        rect = Rectangle(10, 20)
        rect.update(id=1, width=15, height=25, x=3, y=4)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_to_dictionary(self):
        """Test the to_dictonary methode of Rectangle class"""
        r = Rectangle(5, 10, 1, 2, 3)
        d = {'x': 1, 'y': 2, 'id': 3, 'height': 10, 'width': 5}
        self.assertEqual(r.to_dictionary(), d)

    def test_init_with_invalid_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 20)

    def test_init_with_invalid_height(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, -5)

    def test_init_with_invalid_x(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 20, -1)

    def test_init_with_invalid_y(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 20, 2, -1)

    def test_init_with_non_integer_width(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("invalid_width", 10)

    def test_init_with_non_integer_height(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, "invalid_height")

    def test_init_with_non_integer_x(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, 20, "invalid_x")

    def test_init_with_non_integer_y(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, 20, 2, "invalid_y")

    def test_init_with_negative_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-5, 10)

    def test_init_with_zero_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 10)


if __name__ == "__main__":
    unittest.main()
