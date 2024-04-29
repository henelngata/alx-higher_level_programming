#!/usr/bin/usr/python3

"""contains tests for Base class
"""
import unittest
from models.base import Base 

class TestBaseClass(unittest.TestCase):
    def test_id_generation(self):
        # Create instances of Base and check if IDs are assigned correctly
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_custom_id(self):
        # Create an instance with a custom ID
        custom_base = Base(id=10)
        self.assertEqual(custom_base.id, 10)