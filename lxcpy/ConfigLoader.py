"""
This module helps to loads and parse a json config file
"""


import json
from .ConfigValidator import validate
from .Utils import exit

required = ["name", "image", "componentsPath"]


def loads_json(file_path=""):
    """
    Reads a config.json file and validates it
    Returns a valid dict
    """
    try:
        file = open(file_path, "r")
        data = file.read()
        try:
            dict_data = json.loads(data)
            is_valid = validate(required, dict_data, raise_exception=True)
            return dict_data
        except json.decoder.JSONDecodeError as e:
            error_msg = "Error en el archivo {} ...\n\n{}".format(
                file_path, str(e)
            )
            exit(error_msg)
        except Exception as e:
            exit(str(e))
    except FileNotFoundError as e:
        exit(str(e))
