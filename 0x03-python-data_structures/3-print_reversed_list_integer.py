#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        for el in my_list[::-1]:
            print("{:d}".format(el))