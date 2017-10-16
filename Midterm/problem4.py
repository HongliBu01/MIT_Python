#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:12:33 2017

@author: bhl
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    triang_num = 0
    count = 1
    while k > triang_num:
        triang_num += count
        count += 1
    if k == triang_num:
        return True
    return False

print(str(is_triangular(500501)))
