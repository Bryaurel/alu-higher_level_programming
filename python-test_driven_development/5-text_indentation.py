#!/usr/bin/python3
"""prints a text with 2 new lines"""


def text_indentation(text):
    """ Prints a text with 2 new lines
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
