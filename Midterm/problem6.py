#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 14:09:12 2017

@author: bhl
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    times = []
    for i in range(len(L)):
        times.append(1)
    L.sort()
    L.reverse()
    if len(L) == 1:
        return L[0]
    for i in range(0,len(L) - 1):
        if L[i] == L[i+1]:
            times[i+1] = times[i] + 1
        if L[i] > L[i+1] and times[i]%2 != 0:
            return L[i]
        elif L[i] == L[i+1] and i+1 == (len(L) - 1):
            return None
        elif L[i] > L[i+1] and i+1 == (len(L) - 1):
            return L[i+1]
    

print(largest_odd_times([2, 2, 3]))