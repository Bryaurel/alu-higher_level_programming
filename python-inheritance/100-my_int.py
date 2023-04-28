#!/usr/bin/python3
"""write a class myint"""


class MyInt(int):
    """ class MyInt that inherits from int """
    def __eq__(self, other):
        """ equal (=) inverted """
        return False

    def __ne__(self, other):
        "not equal (!=) inverted """
        return True
