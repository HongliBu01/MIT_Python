#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 23:58:35 2017

@author: bhl
"""
'''
def f(stuff):
    for thing in stuff:
        if thing == 'iQ':
            print("Found it")

f("iQ")
'''

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x
print(str(Square(-15)))
