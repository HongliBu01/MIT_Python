#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 00:32:47 2017

@author: bhl
"""

def oddTuples(aTup):
    oddtuple = ()
    count = 1
    for t in aTup:
        if count % 2 != 0:
            oddtuple = oddtuple + (t,)
        count += 1
    return oddtuple



'''
def oddTuples(aTup):
    return aTup[::2]
'''

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))