#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 17:32:17 2017

@author: bhl
"""
        
balance = 320000
annualInterestRate = 0.2

months =12
monthlyInterestRate = annualInterestRate / 12
lo = balance / 12
hi = balance*(1 + monthlyInterestRate) ** months / 12
remaining_b = balance
epsilon = -0.01

monthlyPayment = (hi + lo) / 2
while  remaining_b > 0 or remaining_b < epsilon:
    remaining_b = balance  
    for i in range(months):
        remaining_b = (remaining_b - monthlyPayment) * (1 + annualInterestRate / 12)
    if remaining_b > 0:
        lo = monthlyPayment
    if remaining_b < epsilon:
        hi = monthlyPayment 
    monthlyPayment = (hi + lo) / 2

print("Lowest Payment: ", round(monthlyPayment,2))