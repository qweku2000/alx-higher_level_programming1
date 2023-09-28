#!/usr/bin/python3

"""

The "0-add_integer_module" module 

The module adds two integers and returns the result

"""

def add_integer(a,b):
    if type(a) is not int and type(a) is not float:
       raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
       raise TypeError("b must be an int")

    if type(a) is float:
       a = int(a)
    if type(b) is float:
       b = int(b)

    return a+b
