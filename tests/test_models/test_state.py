#!/usr/bin/python3
"""Test case for state model"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Test for state class"""

    def __init__(self, *args, **kwargs):
        """Init to set up test environment"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test for name attribute"""
        new = self.value()
        self.assertNotEqual(type(new.name), str)

    def test_to_dictstate(self):
        """test to dict method with state and the type and content"""
        state = State()
        dict_cont = state.to_dict()
        self.assertEqual(type(dict_cont), dict)
        for attr in state.__dict__:
            self.assertTrue("__class__" in dict_cont)

    def test_dict_value(self):
        """test the returned dictionar values"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        state = State()
        dict_con = state.to_dict()
        self.assertEqual(dict_con["__class__"], "State")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
            dict_con["created_at"],
            state.created_at.strftime(time_format)
        )
        self.assertEqual(
            dict_con["updated_at"],
            state.updated_at.strftime(time_format))
