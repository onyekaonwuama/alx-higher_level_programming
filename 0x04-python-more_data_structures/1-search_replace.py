#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_copy = []
    for i in range(len(my_list)):
        if my_list[i] == search:
           my_copy.append(replace)
        else:
            my_copy.append(my_list[i])
    return my_copy
