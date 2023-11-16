#!/usr/bin/python3
"""class MyList"""


class MyList(list):
    """
    Defines class Mylist that inherits from list
    """
    def print_sorted(self):
        """
        public method that prints the list
        but sorted (ascending sort)
        """
        print(sorted(self))
