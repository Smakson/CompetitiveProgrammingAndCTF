# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:53:14 2017

@author: Miha
"""


def multiples_up_to(x, a):
    """Returns a list of multiples of the number 'x'
    such that all the multiples are strictly smaller than
    an integer 'a'"""
    return [x * i for i in range(a) if i * x < a]


def list_intersection(a, b):
    """Given two lists 'a' and 'b' it returns a new list
    that hold elements which are in both 'a' and 'b' - 
    the intersection"""
    return [x for x in a if x in b]    


def list_union(a, b):
    """Given two lists 'a' and 'b' it returns a new list
    that hold elements which are in both 'a' and 'b' - 
    the intersection"""
    temp = [x for x in a]
    for x in b:
        if x not in temp:
            temp.append(x)
    return temp


