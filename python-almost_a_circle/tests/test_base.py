#!/usr/bin/python3
"""

A python unittest for class base

"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_base(unittest.TestCase):
    """
    Class for unittest
    """
    def test_id_None(self):
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        b = Base(27)
        self.assertEqual(27, b.id)

    def test_multiple_id(self):
        b1 = Base()
        b2 = Base(27)
        b3 = Base()
        self.assertEqual(2, b1.id)
        self.assertEqual(27, b2.id)
        self.assertEqual(3, b3.id)

    def test_id_zero(self):
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_negatif_id(self):
        b = Base(-7)
        self.assertEqual(-7, b.id)

    def test_float_id(self):
        b = Base(7.7)
        self.assertEqual(7.7, b.id)

    def test_string_id(self):
        b = Base("abc")
        self.assertEqual("abc", b.id)

    def test_list_id(self):
        b = Base([1])
        self.assertEqual([1], b.id)

    def test_empty_list_id(self):
        b = Base([])
        self.assertEqual([], b.id)

    def test_tuple_id(self):
        b = Base((1, 2, 3))
        self.assertEqual((1, 2, 3), b.id)

    def test_dictonary_id(self):
        b = Base({"a": 1, "b": 2, "c": 3})
        self.assertEqual({"a": 1, "b": 2, "c": 3}, b.id)

    def test_to_many_arg_id(self):
        with self.assertRaises(TypeError):
            b = Base(1, 2)

    def test_to_json_string_empty_list(self):
        """Test to_json_string with empty list"""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty_list(self):
        """Test to_json_string with non-empty list"""
        result = Base.to_json_string([{'key': 'value'}])
        self.assertEqual(result, '[{"key": "value"}]')

    def test_from_json_string_empty_string(self):
        """Test from_json_string with empty string"""
        result = Base.from_json_string('')
        self.assertEqual(result, [])

    def test_from_json_string_non_empty_string(self):
        """Test from_json_string with non-empty string"""
        result = Base.from_json_string('[{"key": "value"}]')
        self.assertEqual(result, [{'key': 'value'}])
