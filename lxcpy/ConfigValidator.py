"""
This function validates a dictionary has some required values
"""


def validate(required, dict_data=None, raise_exception=False):
    dict_type = type(dict_data)
    valid = True

    if dict_type is not dict:
        if raise_exception is True:
            raise Exception("No se puede validar {}".format(dict_type))
        else:
            return False

    for req in required:
        if dict_data.get(req) is None:
            if raise_exception is True:
                raise Exception("Falta el campo: {}".format(req))
            else:
                valid = False
                break
    return valid
