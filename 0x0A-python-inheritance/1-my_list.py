#!/usr/bin/python3

"""Defines a class MyList that inherits from lists ."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints a a sorted list (ascending)."""
        print(sorted(self))
