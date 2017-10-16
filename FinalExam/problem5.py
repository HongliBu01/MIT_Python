#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 15:59:45 2017

@author: bhl
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    map = {}
    decode = ""
    for i in range(len(map_from)):
        map[map_from[i]] = map_to[i]
    for letter in code:
        for key in map:
            if map[key] == letter:
                decode += key
    return (map, decode)

print(cipher("abcd", "dcba", "dab"))