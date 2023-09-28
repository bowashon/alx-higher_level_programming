#!/usr/bin/python3
"""function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """
    Definition:
        Defines a function that appends new_string after search_string
    Args:
        filename"": the name of the file
        search_sting: string to append after
        new_string: new_string to be appended
    """
    content = []

    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            content.append(line)

            if search_string in line:
                content.append(new_string)

    with open(filename, 'w', encoding='UTF-8') as file:
        file.writelines(content)
