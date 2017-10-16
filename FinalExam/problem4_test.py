#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 01:46:43 2017

@author: bhl
"""
'''
def flatten(t):
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
'''
result = []
def flatten(t):
    if isinstance(t, int):
        result.append(t)
    elif isinstance(t, (list, tuple)):
        for item in t:
            flatten(item)
        return result
    return result
        
t = 1   
print(flatten(t)) 