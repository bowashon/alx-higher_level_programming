#!/usr/bin/python3
"""The test indentation module"""


def text_indentation(text):
    """
    Definition:
        Defines a function that prints a text with 2 new lines after
        each of these characters: ., ? and :
    Arg:
        text: points to the text string
    Raise:
        TypeError: text must be a string. if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
                    [line.strip(" ") for line in text.split(delim)])

    print(text, end='')
