# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:32:01 2017

@author: Miha
"""



def factors(x):
    if is_prime(x):
        return [1, x]
    temp = [1]
    primes = list_primes(x)
    t = x
    for prime in primes:
        if t % prime == 0:
            temp.append(prime)
            t = t // prime
    return temp   
        