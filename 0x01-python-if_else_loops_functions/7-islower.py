#!/usr/bin/python3
def islower(c):
    a = 97
    while a < 123:
        if ord(c) == a:
            return True
        a += 1
        return False
