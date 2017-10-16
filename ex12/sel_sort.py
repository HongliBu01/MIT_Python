#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 10:53:04 2017

@author: bhl
"""

def sel_sort(L):
    surfix = 0
    while surfix != len(L):
        for i in range(surfix, len(L)):
            if L[surfix] < L[i]:
                L[surfix], L[i] = L[i], L[surfix]
        surfix += 1
    return L

L = [1,4,2,5,7,8,6,3,9,0]
print(sel_sort(L))