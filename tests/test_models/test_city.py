#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.base_model import BaseModel, Base
import unittest


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

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
            self.assertTrue('name' in self.my_place.__dir__())
            self.assertTrue('state_id' in self.my_place.__dir__())
