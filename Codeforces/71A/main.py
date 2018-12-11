# -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:38:50 2018

@author: Miha
"""
def abbreviate(string):
    l = len(string)
    if l <= 10:
        return string
    else:
        return string[0] + str(l - 2) + string[l-1]
num = int(input())
words = []
for i in range(num):
    string = input()
    words.append(string)
    
for word in words:
    print(abbreviate(word))
    