#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:30:26 2017

@author: bhl
"""

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    list_s = list(s) 
    for letter in s:
        if letter.lower() in "aeiou":
            list_s.remove(letter)
    print("".join(list_s))

print_without_vowels("THIs is great")