#!/usr/bin/python3
# Tests for class Review
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_properties(self):
        review = Review()
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_default_value(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_assigned_value(self):
        review = Review()
        review.place_id = "345"
        review.user_id = "123"
        review.text = "mane"
        self.assertEqual(review.place_id, "345")
        self.assertEqual(review.user_id, "123")
        self.assertEqual(review.text, "mane")


if __name__ == '__main__':
    unittest.main()
