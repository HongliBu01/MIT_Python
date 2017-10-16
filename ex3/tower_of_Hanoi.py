#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 12:24:19 2017

@author: bhl
"""
count = 0

def printmove(fr, to):
    global count
    print("Move from " + str(fr) + " to " + str(to))
    count += 1
    
    


def towermove(n, fr, to, spare):
    '''
    n gonna be int
    
    '''
    if n == 1:
        printmove(fr, to)
    else:
        towermove(n-1, fr, to, spare)
        towermove(1, fr, spare, to)
        towermove(n-1, to, spare, fr)

towermove(2, "p1", "p2", "p3")
print ("count = ", count)