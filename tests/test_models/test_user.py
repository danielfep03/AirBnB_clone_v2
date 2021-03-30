#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models.base_model import BaseModel, Base
import unittest


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

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
