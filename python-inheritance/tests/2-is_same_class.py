#!/usr/bin/python3
""" The program validates that object is exactly the same """


def is_same_class(obj, a_class):
    """ Returns True if the object is exactly an
    instance of the specified class ; otherwise False. """
    if (type(obj) == a_class):
        return True
    return False