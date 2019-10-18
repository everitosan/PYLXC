"""
Test the config loader
"""
# python
import unittest

from lxcpy.ConfigLoader import loads_json

base_path = __file__[:-14]


class TestLoader(unittest.TestCase):
    def test_exit_file_not_found(self):
        with self.assertRaises(SystemExit):
            loads_json("")

    def test_exit_required_not_found(self):
        with self.assertRaises(SystemExit):
            path = "{}bad_config.json".format(base_path)
            loads_json(path)

    def test_loads(self):
        path = "{}config.json".format(base_path)
        res = loads_json(path)
        self.assertEqual(type(res), dict)
