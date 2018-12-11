# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 21:58:48 2018

@author: Miha
"""

s = input()
t = input()
moves = 0
ls = len(s)
lt = len(t)
ml = min(ls, lt)
i = 1
while i <= ml and s[-i] == t[-i]:
    i += 1
i -= 1
if i == 0:
    g = ''
else:
    g = s[-i:] 
lg = len(g)

moves = ls + lt - 2*lg
print(moves)
