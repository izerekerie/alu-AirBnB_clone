#!/usr/bin/python3
import unittest
from models.city import City


class CityTest(unittest.TestCase):
    def test_properties(self):
        city = City()
        self.assertTrue(hasattr(city, 'name'))
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))

    def test_default_value(self):
        city = City()
        self.assertEqual(city.name, "")

    def test_assigned_value(self):
        city = City()
        city.name = "Kigali"
        city.id = "123"
        self.assertEqual(city.name, "Kigali")
        self.assertEqual(city.id, "123")


if __name__ == '__main__':
    unittest.main()
