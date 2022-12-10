#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for new_key in a_dictionary:
            if new_key == key:
                a_dictionary[new_key] = value
    return a_dictionary
