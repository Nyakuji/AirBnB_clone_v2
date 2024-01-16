#!/usr/bin/python
"""Test case for User model"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Test cases for the User class """

    def __init__(self, *args, **kwargs):
        """Init to Set up test environment """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test first_name attribute"""
        new = self.value()
        self.assertNotEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test last_name attribute"""
        new = self.value()
        self.assertNotEqual(type(new.last_name), str)

    def test_email(self):
        """Test email attribute"""
        new = self.value()
        self.assertNotEqual(type(new.email), str)

    def test_password(self):
        """Test password attribute"""
        new = self.value()
        self.assertNotEqual(type(new.password), str)

    def test_to_dictUser(self):
        """test to dict method with user and the type and content"""
        user = User()
        dict_cont = user.to_dict()
        self.assertEqual(type(dict_cont), dict)
        for attr in user.__dict__:
            self.assertTrue("__class__" in dict_cont)

    def test_dict_value(self):
        """test the returned dictionar values"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        user = User()
        dict_con = user.to_dict()
        self.assertEqual(dict_con["__class__"], "User")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
            dict_con["created_at"],
            user.created_at.strftime(time_format)
        )
        self.assertEqual(
            dict_con["updated_at"],
            user.updated_at.strftime(time_format))    
