#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_properties(self):
        amenity = Amenity()  # Instance variable should be lowercase
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))

    def test_default_value(self):
        amenity = Amenity()  # Instance variable should be lowercase
        self.assertEqual(amenity.name, "")  # Test for default value of 'name'

    def test_assigned_value(self):
        amenity = Amenity()  # Instance variable should be lowercase
        amenity.name = "amenity"
        self.assertEqual(amenity.name, "amenity")  # Test for assigned value of 'name'


if __name__ == '__main__':
    unittest.main()
