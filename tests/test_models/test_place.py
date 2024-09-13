#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):

    def test_properties(self):
        place = Place()
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))  # Consistent name
        self.assertTrue(hasattr(place, 'amenity_ids'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue(hasattr(place, 'user_id'))  # Added user_id

    def test_default_value(self):
        place = Place()
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.latitude, 0.00)
        self.assertEqual(place.longitude, 0.00)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.number_bathrooms, 0)  # Consistent name
        self.assertEqual(place.amenity_ids, [])

    def test_assigned_value(self):
        place = Place()
        place.user_id = "123"
        place.name = "Mane"
        place.description = "parallel to name"
        place.latitude = 1.00
        place.longitude = 0.01
        place.city_id = "321"
        place.max_guest = 3
        place.number_rooms = 2
        place.number_bathrooms = 1  # Consistent name
        place.amenity_ids = ["2", "4", "54"]
        place.price_by_night = 4500
        self.assertEqual(place.user_id, "123")
        self.assertEqual(place.name, "Mane")
        self.assertEqual(place.description, "parallel to name")
        self.assertEqual(place.latitude, 1.00)
        self.assertEqual(place.longitude, 0.01)
        self.assertEqual(place.city_id, "321")
        self.assertEqual(place.max_guest, 3)
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.amenity_ids, ["2", "4", "54"])
        self.assertEqual(place.price_by_night, 4500)


if __name__ == '__main__':
    unittest.main()
