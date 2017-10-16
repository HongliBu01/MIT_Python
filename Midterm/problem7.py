#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 16:38:24 2017

@author: bhl
"""


def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    invert_d ={}
    for key in d.keys():
        if d[key] in invert_d.keys():
            invert_d[d[key]].append(key)
        else:
            a = []
            a.append(key)
            invert_d[d[key]] = a
    for value in invert_d.values():
        value.sort()
    return invert_d
            
d = {1:10, 2:20, 3:30, 4:30}

print(dict_invert(d))