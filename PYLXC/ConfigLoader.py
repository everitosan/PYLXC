import json
from Logger import error as log_error


def loads_json(file_path=""):
    file = open(file_path, "r")
    data = file.read()
    try:
        return json.loads(data)
    except json.decoder.JSONDecodeError as e:
        error_msg = "Error en el archivo {} ...\n\n{}".format(
            file_path, str(e)
        )
        log_error(error_msg)
