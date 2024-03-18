#!/usr/bin/python3

"""
Testing city
"""
import unittest
import os
from models.city import City
from models.base_model import BaseModel
import pep8
from os import getenv


class TestCity(unittest.TestCase):
    """
    Testing the city class
    """

    @classmethod
    def setUpClass(cls):
        """
        set up for test
        """
        cls.city = City()
        cls.city.name = "NY"
        cls.city.state_id = "TX"

    @classmethod
    def teardown(cls):
        """
        Tear down at the end of the test
        """
        del cls.city

    def tearDown(self):
        """
        Teardown
        """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_City(self):
        """
        Checking for docstrings
        """
        self.assertIsNotNone(City.__doc__)

    def test_is_subclass_City(self):
        """
        Testing if City is a subclass of Basemodel
        """
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attributes_City(self):
        """
        Do city have attributes?
        """
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_attribute_types_City(self):
        """
        Testing the attribute type for City
        """
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db',
                     "can't")
    
    def test_to_dict_City(self):
        """
        Testing if dictionary works
        """
        self.assertEqual('to_dict' in dir(self.city), True)

    def test_save_City(self):
        """
        Testing if the save works
        """
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

if __name__ == "__main__":
    unittest.main()
