#!/usr/bin/python3
"""Create a square"""


class Square:
    """Private instance attribute: size
    Private instance attribute: position
    Instantation with optional size and optional position:
    Public instance method: def area(self): that returns the square area
    Public instance method: def my_print(self): that prints the square with #:
        no import modules"""

        def __init__(self, size=0, position=(0, 0)):
            self.__size = size
            self.__position = position

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, value):
            if type(value) is not int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

        @property
        def position(self):
            return self.__position

        @position.setter
        def position(self, value):
            if (not isinstance(value, tuple) or
                    len(value) != 2 or
                    not all(isinstance(num, int) for num in value) or
                    not all(num >=0 for num in value)):
                raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

        def area(self):
            return self.size**2

        def my_print(self):
            if self.__size == 0:
                print()
                return
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")
