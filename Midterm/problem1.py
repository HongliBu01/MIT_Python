#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 23:02:55 2017

@author: bhl
"""
'''
x = "pi"
y = "pie"
x,y = y,x
print(x)
print(y)

def f(x):
    while x > 3:
        f(x+1)

f(2)

i = -1
j = 0
while i >= 0:
    while j >= 0:
        print(i, j)
'''
def f(x):
    a = []
    while x > 0:
        a.append(x)
        print (a)
        f(x-1)
        x -= 1

f(3)