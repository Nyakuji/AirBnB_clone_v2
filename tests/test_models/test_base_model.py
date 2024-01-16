"""Test Case For Base Model """
from models.base_model import BaseModel
import unittest
from datetime import datetime, timedelta
from uuid import UUID
import json
from unittest import mock
import os
import models


class test_basemodel(unittest.TestCase):
    """Test Case For Base Model"""

    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """set up for testcase """
        self.model = BaseModel()
        

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)
    
    @mock.patch('models.storage')
    def test_instance(self, mock_storage):
        """
            Testing Base Model Class
        """
        instance = BaseModel()
        self.assertIs(type(instance), BaseModel)
        instance.name = "Philip"
        instance.phone = 3838
        type_attr = {
            "id": str,
            "updated_at": datetime,
            "created_at": datetime,
            "name": str,
            "phone": int
        }
        for attr, type_at in type_attr.items():
            with self.subTest(attr=attr, typ=type_at):
                self.assertIn(attr, instance.__dict__)
                self.assertIs(type(instance.__dict__[attr]), type_at)
        self.assertTrue(mock_storage.new.called)
        self.assertEqual(instance.name, "Philip")
        self.assertEqual(instance.phone, 3838)
    
    def test_uuid(self):
        """
            Test different UUID for different instances
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)
        uuid = instance1.id
        with self.subTest(uuid=uuid):
            self.assertIs(type(uuid), str)
    
    def test_datetime(self):
        """
        Test different instance, different time.
        Test same created at and updated when instance is created.
        """
        tc_before = datetime.now()
        instance1 = BaseModel()
        tc_after = datetime.now()
        self.assertTrue(tc_before <= instance1.created_at <= tc_after)
        time.sleep(1e-4)
        instance2 = BaseModel()
        self.assertEqual(instance1.created_at, instance1.updated_at)
        self.assertNotEqual(instance1.created_at, instance2.created_at)
        self.assertNotEqual(instance1.updated_at, instance2.updated_at)
    
    def test_to_dict(self):
        """
            Test to_dict method in base model
        """
        instance = BaseModel()
        instance.name = "Philip"
        instance.num = 38
        dict_inst = instance.to_dict()
        attribute = [
            "id",
            "created_at",
            "updated_at",
            "name",
            "num",
            "__class__"]
        self.assertCountEqual(dict_inst.keys(), attribute)
        self.assertEqual(dict_inst['__class__'], 'BaseModel')
        self.assertEqual(dict_inst['name'], "Philip")
        self.assertEqual(dict_inst['num'], 38)
    
    def test_created_at_is_current_time(self):
        """ Test if created_at is set to the current time """
        self.assertIsInstance(self.model.created_at, datetime)
    
    def test_updated_at_is_current_time_after_save(self):
        """ Test if updated_at is set to the current time after save """
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(initial_updated_at, self.model.updated_at)
        self.assertIsInstance(self.model.updated_at, datetime)
    
    def test_delete_method(self):
        """ Test if delete method removes the instance from storage """
        models.storage.new(self.model)
        models.storage.save()
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, models.storage.all())
        self.model.delete()
        self.assertNotIn(key, models.storage.all())
    
    def test_to_dict_value(self):
        """
            Test that to_dict returns correct values
        """
        time_f = "%Y-%m-%dT%H:%M:%S.%f"
        instance = BaseModel()
        dict_base = instance.to_dict()
        self.assertEqual(dict_base["__class__"], "BaseModel")
        self.assertEqual(type(dict_base["created_at"]), str)
        self.assertEqual(type(dict_base["updated_at"]), str)
        self.assertEqual(
            dict_base["created_at"],
            instance.created_at.strftime(time_f)
        )
        self.assertEqual(
            dict_base["updated_at"],
            instance.updated_at.strftime(time_f)
        )
    
    @mock.patch("models.storage")
    def test_save(self, mock_storage):
        """
            Test save and update_at is working and storage save call
        """
        instance = BaseModel()
        old_value_created = instance.created_at
        old_value_update = instance.updated_at
        instance.save()
        new_value_created = instance.created_at
        new_value_updated = instance.updated_at
        self.assertNotEqual(old_value_update, new_value_updated)
        self.assertEqual(old_value_created, new_value_created)
        self.assertTrue(mock_storage.save.called_once)