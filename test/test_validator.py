# python
import unittest

# Modules
from lxcpy.ConfigValidator import validate

required = ["name", "image", "componentsPath"]

bad_dict = {
    "name": "some",
    "componentsPath": "some"
}
good_dict = {
    "name": "some",
    "image": "some",
    "componentsPath": "some"
}


class TestValidator(unittest.TestCase):
    def test_required(self):

        res = validate(required, good_dict)
        self.assertTrue(res)

    def test_required_fails(self):
        res = validate(required, bad_dict)
        self.assertFalse(res)

    def test_required_fails_raise(self):
        with self.assertRaises(Exception):
            validate(required, bad_dict, True)
