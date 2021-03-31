#!/usr/bin/python3
""" Module to test users"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models.base_model import BaseModel, Base
import unittest


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
        self.assertTrue('email' in self.my_place.__dir__())
        self.assertTrue('password' in self.my_place.__dir__())
