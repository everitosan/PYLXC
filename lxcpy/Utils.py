import sys
from .Logger import error as log_error


def exit(msg=""):
    log_error(msg)
    log_error("Terminando")
    sys.exit(1)
