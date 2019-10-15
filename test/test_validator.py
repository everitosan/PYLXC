# python
import unittest

# Modules
from PYLXC.ConfigValidator import validate

required = ["name", "image", "componentsPath"]


class TestValidator(unittest.TestCase):
    def test_required(self):
        dict_data = {
            "name": "some",
            "image": "some",
            "componentsPath": "some"
        }

        res = validate(required, dict_data)
        self.assertTrue(res)

    def test_required_fails(self):
        dict_data = {
            "name": "some",
            "componentsPath": "some"
        }

        res = validate(required, dict_data)
        self.assertFalse(res)
