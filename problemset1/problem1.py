# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s = 'azcbobobegghakl'
count = 0

for letter in s:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        count += 1
print("Number of vowels: " + str(count))