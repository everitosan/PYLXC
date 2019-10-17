# Python
import sys
import subprocess

# Modules
from .Logger import error


def exit(msg=""):
    error(msg)
    error("Terminando")
    sys.exit(1)


def execute(command, show_log=False):
    p_res = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = p_res.communicate()
    out_str = stdout.decode("utf-8").lower()
    if "error" in out_str:
        exit(out_str)
    if show_log:
        if stderr is None:
            print()
        else:
            print(stderr)
