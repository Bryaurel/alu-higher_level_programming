#!/usr/bin/python3
"""Create a square"""


class Square:
    """Private instance attribute: size
    Instantiation with size (no type/value verification)
    no importation of modules"""
    def __init__(self, size):
        self.__size = size
