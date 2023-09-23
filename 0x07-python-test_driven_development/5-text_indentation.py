#!/usr/bin/python3
"""function that puts a new line in a text"""


def text_indentation(text):
    """
    Definition: function tha put newline in text
                when ., or > is encountered
    Args:
        text: the function takes text as input
    
    Return: the string with new line spaces
    """
    delim = ". : ?"

    i = 0
    while i < len(text):
        if text[i] in delim:
            print(text[i] + '\n\n', end='')
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            print(text[i], end='')
            i += 1
    
    if __name__ == "__main__":
        import doctest
        doctest.textfile("tests/5-text_indentation.txt")
