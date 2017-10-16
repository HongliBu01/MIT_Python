#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 14:46:54 2017

@author: bhl
"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    sum = 0
    str = ""
    try:
        for letter in s:
            if letter in "0123456789":
                str = letter
                sum += int(letter)
        int(str)  
        return sum    
    except:
        raise ValueError("No digits!")


s = ",fm"     
print(sum_digits(s))