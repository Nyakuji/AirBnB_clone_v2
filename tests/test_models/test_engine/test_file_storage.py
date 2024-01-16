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
        storage = FileStorage()
        new = BaseModel()
        new.save()

        # Find the new object in the storage
        temp = None
        for obj in storage.all().values():
            if obj.id == new.id:
                temp = obj
                break

        self.assertIsNotNone(temp)
        self.assertEqual(new.id, temp.id)
    
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
        storage = FileStorage()
        new = BaseModel()
        new.save()

        original_id = new.id
        storage.reload()

        # Find the reloaded object in the storage
        loaded = None
        for obj in storage.all().values():
            if obj.id == original_id:
                loaded = obj
                break

        # Ensure that the object was successfully reloaded
        self.assertIsNotNone(loaded)

        # Compare the attributes of the original and loaded objects
        self.assertEqual(new.id, loaded.id)
        self.assertEqual(new.to_dict()['created_at'], loaded.to_dict()['created_at'])
        self.assertEqual(new.to_dict()['updated_at'], loaded.to_dict()['updated_at'])
    
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
        storage = FileStorage()
        new = BaseModel()
        _id = new.to_dict()['id']
        temp = None

        # Find the key in storage.all().keys()
        for key in storage.all().keys():
            if key.endswith('.' + _id):
                temp = key
                break

        # Ensure that the key is properly formatted
        self.assertIsNotNone(temp)
        self.assertEqual(temp, 'BaseModel.' + _id)
    
    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)