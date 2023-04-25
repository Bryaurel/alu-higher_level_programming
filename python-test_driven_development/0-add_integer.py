#!/usr/bin/python3
"""adds 2 integers"""


def add_interger(a, b=98):
    """a function that adds two integers
    Args:
    a: must be an integer or float
    b: must be an integer or float
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")

    return a + b
