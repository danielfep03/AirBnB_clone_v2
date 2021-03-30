#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.base_model import BaseModel, Base
import unittest


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

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
