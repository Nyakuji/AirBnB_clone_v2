""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import models


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
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

    def test_created_at_is_current_time(self):
        """ Test if created_at is set to the current time """
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertAlmostEqual(
            self.model.created_at, datetime.utcnow(), delta=datetime.timedelta(seconds=1)
        )
    
    def test_updated_at_is_current_time_after_save(self):
        """ Test if updated_at is set to the current time after save """
        initial_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, initial_updated_at)
        self.assertAlmostEqual(
            self.model.updated_at, datetime.utcnow(), delta=datetime.timedelta(seconds=1)
        )
    
    def test_delete_method(self):
        """ Test if delete method removes the instance from storage """
        models.storage.new(self.model)
        models.storage.save()
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, models.storage.all())
        self.model.delete()
        self.assertNotIn(key, models.storage.all())