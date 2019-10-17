from colorama import Fore, Back, Style


def info(msg):
    print(Fore.GREEN+msg)
    print(Style.RESET_ALL)


def warn(msg):
    print(Fore.YELLOW+msg)
    print(Style.RESET_ALL)


def error(msg):
    print(Fore.RED+msg)
    print(Style.RESET_ALL)
