# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 16:53:00 2018

@author: Miha
"""

n = input()
n = int(n)

a = input()
b = input()

def add(dic, item, value):
    if item not in dic.keys():
        dic[item] = [value]
    else:
        dic[item].append(value)

dicta = dict()
dictb = dict()

    
for i in range(n):
    add(dicta, a[i], i)
    add(dictb, b[i], i)


