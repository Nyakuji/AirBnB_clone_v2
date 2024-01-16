#!/usr/bin/python3
"""Test For Amenity Model"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test For Amenity Class"""

    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test for name attribute"""
        new = self.value()
        self.assertNotEqual(type(new.name), str)

    def test_to_dictAmenity(self):
        """test to dict method with Amenity and the type and content"""
        insta = Amenity()
        dict_cont = insta.to_dict()
        self.assertEqual(type(dict_cont), dict)
        for attr in insta.__dict__:
            self.assertTrue("__class__" in dict_cont)

    def test_dict_value(self):
        """test the returned dictionar values"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        insta = Amenity()
        dict_con = insta.to_dict()
        self.assertEqual(dict_con["__class__"], "Amenity")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
            dict_con["created_at"],
            insta.created_at.strftime(time_format)
        )
        self.assertEqual(
            dict_con["updated_at"],
            insta.updated_at.strftime(time_format))
