# -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:17:13 2018

@author: Miha
"""


numbers = input().split()

a = int(numbers[2]) 
n = int(numbers[0])
m = int(numbers[1])

vnum = m/a
hnum = n/a

ivnum = int(vnum)
ihnum = int(hnum)

if not vnum - ivnum == 0.0:
    ivnum = int(vnum) + 1
    
if not hnum - ihnum == 0.0:
    ihnum = int(hnum) + 1

print(ivnum * ihnum)