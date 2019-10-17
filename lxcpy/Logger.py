"""
Logger module
"""
# Modules
from colorama import Fore, Back, Style


def info(msg, deco=True):
    deco_str = "===>" if deco else ""
    cmpsd_msg = "{}{} {}".format(Fore.GREEN, deco_str, msg)
    print(cmpsd_msg)
    print(Style.RESET_ALL)


def warn(msg, deco=True):
    deco_str = "[!] > " if deco else ""
    cmpsd_msg = "{}{} {}".format(Fore.YELLOW, deco_str, msg)
    print(cmpsd_msg)
    print(Style.RESET_ALL)


def error(msg):
    print(Fore.RED+msg)
    print(Style.RESET_ALL)
