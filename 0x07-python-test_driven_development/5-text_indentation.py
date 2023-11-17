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
    
    characters = ('.', '?', ':')
    new_text = ""

    for char in text:
        new_text += char
        if char in characters:
            del(char)
        new_text += char + '\n\n'
    print(new_text, end='')
