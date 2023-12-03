#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    new = []
    for i in range(len(my_list)):
        new.append(my_list[i])
    new[idx] = element
    return (new)
