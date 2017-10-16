#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:34:58 2017

@author: bhl
"""

def bisection_search(L, e):
    def bisection_search_helper(L, e, low, high):
        if low == high:
            return L[low] == e
        
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid :
                return False
            else:
                return bisection_search_helper(L, e, low, mid - 1)
        else:
            return bisection_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisection_search_helper(L, e, 0, len(L) - 1)

L = [1,2,3,45]    
e = 45            
print(bisection_search(L, e))