# Python
import sys
import subprocess
from .Arguments import parse as parse_arguments

# Modules
from .Logger import error, info, warn


def exit(msg=""):
    error(msg)
    error("Terminando")
    sys.exit(1)


def execute(command, show_log=False):
    """
    Execute commands with help of subprocess and print ouput based on show_log
    and verbode argument
    """
    show_verbose = parse_arguments().verbose

    if show_verbose or show_log:
        warn(" ".join(command))
        res = subprocess.call(command)
        if res != 0:
            exit()
    else:
        p_res = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = p_res.communicate()

        out_str = stdout.decode("utf-8")

        if "Error:" in out_str:
            exit(out_str)
        if stderr is not None:
            exit(stderr)


def print_banner():
    banner = """
     __    _  _  ___  ____  _  _
    (  )  ( \\/ )/ __)(  _ \\( \\/ )
     )(__  )  (( (__  )___/ \\  /
    (____)(_/\\_)\\___)(__)   (__)
    """

    info(banner, False)
