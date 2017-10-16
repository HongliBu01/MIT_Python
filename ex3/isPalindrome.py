#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 16:23:47 2017

@author: bhl
"""

def isPalindrome(s):
    
    def tochar(s):
       s = s.lower()
       ans = ""
       for c in s:
           if c in "abcdefghijklmnopqrstuvwxyz":
               ans += c
       return ans

    def ispal(s):
        if len(s) == 0:
            return True
        elif len(s) == 1:
            return True
        else:
            return s[0] == s[-1] and ispal(s[1:-1])
        
    return ispal(tochar(s))

test_str = "evea"           
print(isPalindrome(test_str))