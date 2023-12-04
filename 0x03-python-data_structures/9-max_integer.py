#!/usr/bin/python3
def max_integer(my_list=[]):
    new = my_list[:]
    if len(new) == 0:
        return None
    else:
        new.sort()
        return (new[-1])
