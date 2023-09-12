#!/usr/bin/python3
"""A class MyList that inherits from List"""


class MyList(list):
    """
        Define a class MyList that inherits from list
    Args:
        int: contains a list of sorted integers
        prints the list to the stdout
    """
    def print_sorted(self):
        """function that sort list and prints it to stdout
        """
        sorted_list = sorted(self)
        print(sorted_list)
