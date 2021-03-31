#!/usr/bin/python3
""" Module to test places"""
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel, Base
from models.place import Place
import unittest
import json
import pep8
import datetime


class Test_place(unittest.TestCase):
    """ Test place """
    def setUp(self):
        """ Test initialization class"""
        self.my_place()

    def test_inheritance(self):
        """ Test inheritance"""
        self.assertIsInstance(self.my_place(), BaseModel)
        self.assertIsInstance(self.my_place(), Base)

    def test_attributes(self):
        """ Test attributes"""
        self.assertTrue('city_id' in self.my_place.__dir__())
        self.assertTrue('user_id' in self.my_place.__dir__())
        self.assertTrue('name' in self.my_place.__dir__())
        self.assertTrue('description' in self.my_place.__dir__())
        self.assertTrue('number_rooms' in self.my_place.__dir__())
        self.assertTrue('number_bathroom' in self.my_place.__dir__())
        self.assertTrue('max_guest' in self.my_place.__dir__())
        self.assertTrue('price_by_night' in self.my_place.__dir__())
        self.assertTrue('latitude' in self.my_place.__dir__())
        self.assertTrue('longitude' in self.my_place.__dir__())

    def test_doc_module(self):
        """Module documentation"""
        doc = Place.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_place(self):
        """Test that models/place.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_place(self):
        """Test that tests/test_models/test_place.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = Place.__init__.__doc__
        self.assertGreater(len(doc), 1)
