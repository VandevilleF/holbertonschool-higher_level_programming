#!/usr/bin/python3
"""

A python unittest for class base

"""


import unittest, os, json
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
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty_list(self):
        result = Base.to_json_string([{'key': 'value'}])
        self.assertEqual(result, '[{"key": "value"}]')

    def test_from_json_string_empty_string(self):
        result = Base.from_json_string('')
        self.assertEqual(result, [])

    def test_from_json_string_non_empty_string(self):
        result = Base.from_json_string('[{"key": "value"}]')
        self.assertEqual(result, [{'key': 'value'}])

    def test_private_nb_objects_no_direct_access(self):
        obj1 = Base()
        with self.assertRaises(AttributeError):
            obj1.__nb_objects

    def test_save_to_file_with_empty_data(self):
        data = []
        filename = "Base.json"
        Base.save_to_file(data)
        with open(filename, 'r', encoding='utf-8') as file:
            saved_data = json.load(file)
            self.assertEqual(saved_data, [])

        os.remove(filename)

    def test_save_to_file_with_none_data(self):
        filename = "Base.json"

        Base.save_to_file(None)

        with open(filename, 'r', encoding='utf-8') as file:
            saved_data = json.load(file)
            self.assertEqual(saved_data, [])

        os.remove(filename)


if __name__ == "__main__":
    unittest.main()
