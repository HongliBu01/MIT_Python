#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 16:54:30 2017

@author: bhl
"""

balance = 3329
annualInterestRate = 0.2

monthlyPayment = 0
months = 12
remaining_b = balance

while remaining_b > 0:
    remaining_b = balance
    monthlyPayment += 10
    for i in range(months):
        remaining_b = (remaining_b - monthlyPayment) * (1 + annualInterestRate / 12)

print("Lowest Payment: ", monthlyPayment)
    
    