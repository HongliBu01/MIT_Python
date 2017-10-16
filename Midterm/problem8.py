#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 16:38:45 2017

@author: bhl
"""

def general_poly (L):
    """ 
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    """
    
    def f(x):
        result = 0
        for i in range(len(L)):
            result += L[i] * (x**(len(L) - i - 1))
        return result
        
    return f

a = general_poly([1, 2, 3, 4])(10)
    
    