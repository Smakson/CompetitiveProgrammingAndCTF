# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 19:25:22 2018

@author: Miha
"""

n = int(input())
a_s = input()
a = a_s.split()
stairways = 0
stairs = []
for i in range(len(a)):
    if a[i] == '1':
        stairways += 1
        stairs.append(a[i - 1])
stairs.append(stairs.pop(0))
print(stairways)
print(' '.join(stairs))


