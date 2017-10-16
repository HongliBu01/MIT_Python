#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 15:50:11 2017

@author: bhl
"""

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 

    def latten(t):
        if isinstance(t, int):
            return [t]
        elif isinstance(t, (list, tuple)):
            result = []
            def update_result(t):
                for item in t:
                    if isinstance(item,(list, tuple)):
                        update_result(item)
                    else:    
                        result.append(item)

            update_result(t)  
            return result

    return max(latten(t))

t = [1,5,[3,6,[7]]]   
print(max_val(t))     

