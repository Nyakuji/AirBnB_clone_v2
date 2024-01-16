#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]
    
    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass
    
    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)
    
    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        obj_ids = [obj.id for obj in storage.all().values()]
        self.assertIn(new.id, obj_ids)
    
    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)
    
    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))
    
    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)
    
    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))
    
    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage._FileStorage__objects = {}
        storage.reload()
        self.assertEqual(len(storage.all()), 1)
        
        loaded = next(iter(storage.all().values()))
        self.assertEqual(new.id, loaded.id)

    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()
    
    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)
    
    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))
    
    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)
    
    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)
    
    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.id  # Assuming BaseModel has an 'id' attribute
        key_to_match = 'BaseModel.' + _id
        
        # Check if the key is present and properly formatted
        self.assertIn(key_to_match, storage.all().keys())
        
        # Optional: Check if there are no extra keys in __objects
        self.assertEqual(len(storage.all()), 1)
    
    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)