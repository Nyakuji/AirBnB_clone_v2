#!/usr/bin/python3
"""Test Case For Review Models"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Test review class"""

    def __init__(self, *args, **kwargs):
        """Init to set up environment for test"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test for place_id attribute"""
        new = self.value()
        self.assertNotEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test for user_id attribute"""
        new = self.value()
        self.assertNotEqual(type(new.user_id), str)

    def test_text(self):
        """Test for text attribute"""
        new = self.value()
        self.assertNotEqual(type(new.text), str)
    
    def test_to_dictReview(self):
        """test to dict method with Review and the type and content"""
        review = Review()
        dict_cont = review.to_dict()
        self.assertEqual(type(dict_cont), dict)
        for attr in review.__dict__:
            self.assertTrue("__class__" in dict_cont)

    def test_dict_value(self):
        """test the returned dictionary values"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        review = Review()
        dict_con = review.to_dict()
        self.assertEqual(dict_con["__class__"], "Review")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
            dict_con["created_at"],
            review.created_at.strftime(time_format)
        )
        self.assertEqual(
            dict_con["updated_at"],
            review.updated_at.strftime(time_format))
