# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:10:47 2017

@author: Miha
"""



def fibonacci_term(x):
    """Returns the x-th term of the
    Fibonacci sequence."""
    if x == 1:
        return 1
    
    if x == 2:
        return 2
    
    return fibonacci_term(x - 1) + fibonacci_term(x - 2)





def fibonacci_generator(a):
    """Returns a list of Fibonacci numbers
    up to the term with the value of an integer a."""
    temp = []
    t = 1
    new = 0
    while new <= a:
        last = fibonacci_term(t)
        temp.append(last)
        t += 1
        new = fibonacci_term(t)
    return temp

def even_filter(l):
    """Takes as an input a list of integers 'l' and returns a list 
    containting only the even integers."""
    return [x for x in l if x % 2 == 0]