#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 19:31:43 2017

@author: bhl
"""

s = "boboobbbbbboobobooboobbegghakl"

bob_num = 0
pre_count_1 = ""
pre_count_2 = ""
for letter in s:      
    if pre_count_1 == "b" and pre_count_2 == "o" and letter == "b":
        bob_num += 1
    pre_count_1 = pre_count_2
    pre_count_2 = letter
        
print("Number of times bob occurs is: " + str(bob_num))