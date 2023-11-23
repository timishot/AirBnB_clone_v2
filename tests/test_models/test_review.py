#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import unittest
import pycodestyle
from models.base_model import BaseModel


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

class Test_PEP8(unittest.TestCase):
    """test review"""
    def test_pep8_user(self):
        """test pep8 user"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Foundcode style errors(and warnings)")


class test_inherit_basemodel(unittest.TestCase):
    """Test if review inherit from BaseModel"""
    def test_instance(self):
        """Checkif user is an instance of BaseModel"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(issubclass(type(review), BaseModel))
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")
