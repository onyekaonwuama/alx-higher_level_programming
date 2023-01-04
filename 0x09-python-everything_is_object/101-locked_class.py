#!/usr/bin/python3
"""Defines a function for locked class."""


class LockedClass:
    """
    Stops the user from instantiating new LockedClass attributes
    for anything except 'first_name' attribute
    """

    __slots__ = ["first_name"]
