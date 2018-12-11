# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 13:21:36 2018

@author: Miha
"""
def IsPw2(n):
    """Returns True or False based on the fact if
    the given input 'n' is a power of 2."""
    return (n & (n - 1)) == 0

n = input()
ass = input()
a = ass.split()
goods = set()
la = len(a)
for i in range(la):
    if i not in goods:
        for j in range(la):
            if i != j and IsPw2(int(a[i]) + int(a[j])):
                goods.add(i)
                goods.add(j)
    
count = la - len(goods)    


print(count)
