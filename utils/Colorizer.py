# Colorizer Library is used by the Printer.py to print colorful text on the terminal
# Created by Luis Castaneda


def black(string):
    string = '\033[30m' + string + '\033[0m'
    return string


def red(string):
    string = '\033[31m' + string + '\033[0m'
    return string


def green(string):
    string = '\033[32m' + string + '\033[m'
    return string


def yellow(string):
    string = '\033[33m' + string + '\033[m'
    return string


def blue(string):
    string = '\033[34m' + string + '\033[m'
    return string


def magenta(string):
    string = '\033[35m' + string + '\033[m'
    return string


def cyan(string):
    string = '\033[36m' + string + '\033[m'
    return string


def white(string):
    string = '\033[37m' + string + '\033[m'
    return string
