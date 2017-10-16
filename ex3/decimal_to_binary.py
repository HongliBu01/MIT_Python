#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 17:19:24 2017

@author: bhl
"""

x = float(input("please input a decimal number between 0 and 1: "))
p = 0
result = ""

while (x*(2**p)) % 1 != 0:
    print("Reminder is :", str(x*(2**p) - int(x*(2**p))))
    p += 1
    
num = int(x*(2**p))

if num == 0:
    result = "0"

while num > 0:
    result = str(num % 2) + result
    num = num // 2    

print("p and result is :" + str(p) + " " + str(len(result)))

for i in range(p - len(result)):
    result = "0" + result
    
result = result[0: -p] + "." + result[-p : ]
print("the binary representation of the decimal number is : ",result)