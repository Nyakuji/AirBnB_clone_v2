#!/usr/bin/python3
"""Test For City Model"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Test for City class"""

    def __init__(self, *args, **kwargs):
        """Initilization"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test for state_id attribute"""
        new = self.value()
        self.assertNotEqual(type(new.state_id), str)

    def test_name(self):
        """Test for name attribute"""
        new = self.value()
        self.assertNotEqual(type(new.name), str)
    def test_to_dictcity(self):
        """
            test to dict method with city and the type
            and content
        """
        city = City()
        dict_cont = city.to_dict()
        self.assertEqual(type(dict_cont), dict)
        for attr in city.__dict__:
            self.assertTrue("__class__" in dict_cont)

    def test_dict_value(self):
        """
            test the returned dictionar values
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        city = City()
        dict_con = city.to_dict()
        self.assertEqual(dict_con["__class__"], "City")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
            dict_con["created_at"],
            city.created_at.strftime(time_format)
        )
        self.assertEqual(
            dict_con["updated_at"],
            city.updated_at.strftime(time_format))
