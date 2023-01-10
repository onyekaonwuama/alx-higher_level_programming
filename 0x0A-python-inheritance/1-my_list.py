#!/usr/bin/python3
"""
Class module that inherits from the list object
"""


class MyList(list):
    """ to sort MyList class """

    def print_sorted(self):
        """ Prints the ascending list"""

        print(sorted(self))
