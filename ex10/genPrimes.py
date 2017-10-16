#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 14:53:07 2017

@author: bhl
"""

def genPrimes():
    prime = []
    num = 1
    
    while num < 100:
        num += 1
        for p in prime:
            if num % p == 0:
                break
        else:
                prime.append(num)
                yield num


