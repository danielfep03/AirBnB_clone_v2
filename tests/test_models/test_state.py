#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.base_model import BaseModel
from models.state import State
import unittest

class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


class MyTestCase(unittest.TestCase):
    """Test State"""
    def test_class(self):
        """Test is Class"""
        my_state = State()
        setattr(my_state, 'name', 'California')
        self.assertIsInstance(my_state, BaseModel)
        self.assertEqual(my_state.name, "California")
