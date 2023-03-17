#!/usr/bin/python3
"""Create a square"""


class Square:
    """Private instance attribute: size
        Instantation with optional size: def __init__(self, size=0)
        Public instance method: def area(self)
        no import module"""

    def __init__(self, size=0):
        self.__size = size

        @property
        def size(self):
            return self.__size

        @size.better
        def size(self, value):
            if type(value) is not int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

        def area(self):
            return self.__size**2
