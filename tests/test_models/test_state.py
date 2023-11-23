#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest
import pycodestyle
from models.base_model import BaseModel


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


class Test_PEP8(unittest.TestCase):
    """test state"""
    def test_pep8_user(self):
        """test pep8 state"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Foundcode style errors(and warnings)")


class test_inherit_basemodel(unittest.TestCase):
    """Test if user inherit from BaseModel"""
    def test_instance(self):
        """Checkif user is an instance of BaseModel"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(issubclass(type(state), BaseModel))
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
