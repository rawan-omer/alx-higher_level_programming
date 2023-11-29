#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) < 123:
            ord(str[i]) -= 32
        else:
            print("{}".format(chr(ord(str[i]))), end="")
    print()
