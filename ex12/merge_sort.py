#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 12:00:18 2017

@author: bhl
"""

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j <len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L):
    if len(L) <= 1:
        return L[:]
    else:
        mid = len(L)//2
        left = merge_sort(L[ : mid])
        right = merge_sort(L[mid : ])
        return merge(left, right)

print(merge_sort([4,1,2,5,6,3,7,0,9,8]))