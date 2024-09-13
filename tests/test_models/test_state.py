#!/usr/bin/python3
# this commands to run script in python3
import unittest
# this is a python built in testing framework which creat a test case to verify if code works as expected
from models.state import State


class TestState(unittest.TestCase):
    def test_properties(self):
        state = State()
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "name"))

    def test_default_value(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_assign_values(self):
        state = State()
        state.name = "stest"
        self.assertEqual(state.name, "stest")


if __name__ == '__main__':
    unittest.main()
