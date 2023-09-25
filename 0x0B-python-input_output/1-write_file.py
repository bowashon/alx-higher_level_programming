# !/usr/bin/python3
"""function that writew a string to a text file"""


def write_file(filename="", text=""):
    """
    Definition:
        Defines a function that writes a string to a text file (UTX8)
    Args:
        filename: string that represent the name of the file to be created
        text: the content to be written to the file
    Return:
        Returns the number of test written
    """

    with open(filename, "w", encoding='UTF-8') as f:

        return f.write(text)
