#!/usr/bin/python3
def no_c(my_string):
    myList = []
    for char in my_string:
        if char != 'c' and char != 'C':
            myList.append(char)
    return ''.join(myList)
