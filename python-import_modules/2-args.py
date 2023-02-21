#!/usr/bin/python3
from sys import argv

if __name == "__main__":
    number_of_args = len(argv) - 1
    if number_of_args > 0:
        if number_of_args == 1:
            print("{} argument:".format(number_of_args))
        else:
            print("{} argument:".format(number_of_args))
        values = 1
        for arg in argv[1:]
        print("{}: {}".format(values, arg))
        values += 1
    else:
        print("{} argument.".format(number_of_args))
