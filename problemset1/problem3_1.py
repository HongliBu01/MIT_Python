#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 21:23:35 2017

@author: bhl
"""
s = 'azcbabcdefghijklmnobobegghakldefghjkl'

count = 0
pre_count = 0
pre_letter = ""
word = ""
pre_word = ""
for letter in s:
    if pre_letter <= letter:
        count += 1
        word = word + letter       
    elif pre_count < count:
        pre_count = count
        pre_word = word
        word = letter
        count = 1
    else :
        word = letter
        count = 1
    pre_letter = letter

if pre_count < count:
    print("Longest substring in alphabetical order is: " + word) 
else:
    print("Longest substring in alphabetical order is: " + pre_word)