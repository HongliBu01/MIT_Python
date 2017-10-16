#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 16:20:14 2017

@author: bhl
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0: 
        return False
    elif len(aStr) == 1:
        return char == aStr
    else:
        return char == aStr[len(aStr)//2] or (char < aStr[len(aStr)//2] and isIn(char, aStr[0 : len(aStr)//2])) or (char > aStr[len(aStr)//2] and isIn(char, aStr[len(aStr)//2 : ]))

print("the char is in the string : ", isIn("s", "abcdghiksxyz"))