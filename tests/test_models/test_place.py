#!/usr/bin/python3
"""Test Case For Place Model"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Test For Place Class"""

    def __init__(self, *args, **kwargs):
        """Init to set up environment for test"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test for city_id attribute"""
        new = self.value()
        self.assertNotEqual(type(new.city_id), str)

    def test_user_id(self):
        """Test for user_id attribute"""
        new = self.value()
        self.assertNotEqual(type(new.user_id), str)

    def test_name(self):
        """Test for name attribute"""
        new = self.value()
        self.assertNotEqual(type(new.name), str)

    def test_description(self):
        """Test for description attribute"""
        new = self.value()
        self.assertNotEqual(type(new.description), str)

    def test_number_rooms(self):
        """Test for number_room attribute"""
        new = self.value()
        self.assertNotEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Test for number_bathrooms attribute"""
        new = self.value()
        self.assertNotEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Test max_guest attribute"""
        new = self.value()
        self.assertNotEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Test for price_by_night attribute"""
        new = self.value()
        self.assertNotEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Test for latitude attribute"""
        new = self.value()
        self.assertNotEqual(type(new.latitude), float)

    def test_longitude(self):
        """Test for longitude attribute"""
        new = self.value()
        self.assertNotEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """Test for amenity_ids attribute"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    def test_to_dictPlace(self):
        """
            test to dict method with Place and the type
            and content
        """
        place = Place()
        dict_cont = place.to_dict()
        self.assertEqual(type(dict_cont), dict)
        for attr in place.__dict__:
            self.assertTrue("__class__" in dict_cont)

    def test_dict_value(self):
        """
            test the returned dictionar values
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        place = Place()
        dict_con = place.to_dict()
        self.assertEqual(dict_con["__class__"], "Place")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
            dict_con["created_at"],
            place.created_at.strftime(time_format)
        )
        self.assertEqual(
            dict_con["updated_at"],
            place.updated_at.strftime(time_format))
