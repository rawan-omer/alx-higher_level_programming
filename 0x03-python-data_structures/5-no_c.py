#!/usr/bin/python3
def no_c(my_string):
    myList = list(my_string)
    for char in myList:
        if char == 'c' or char == 'C':
            myList.remove(char)
    return (myList)
