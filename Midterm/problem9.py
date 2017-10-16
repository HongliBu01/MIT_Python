#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 16:43:22 2017

@author: bhl
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    if L1 == [] and L2 == []:
        return (None, None, None)
    elif len(L1) != len(L2) :
        return False

    element_L1 = []
    count_L1 =[]
    element_L2 = []
    count_L2 = []
    for i in range(len(L1)):
        if L1[i] not in element_L1:
            element_L1.append(L1[i])
            count_L1.append(1)
        else:
            count_L1[element_L1.index(L1[i])] += 1
        if L2[i] not in element_L2:
            element_L2.append(L2[i])
            count_L2.append(1)
        else:
            count_L2[element_L2.index(L2[i])] += 1

    for i in range(len(element_L1)):
        if element_L1[i] not in element_L2:
            return False
        elif element_L2[i] not in element_L1:
            return False
    for element in element_L1:
        if count_L1[element_L1.index(element)] != count_L2[element_L2.index(element)]:
            return False
    
    count_max = max(count_L1) 
    element_max = element_L1[count_L1.index(count_max)]
    
    return (element_max, count_max, type(element_max))


L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']
print(is_list_permutation(L1, L2))
        