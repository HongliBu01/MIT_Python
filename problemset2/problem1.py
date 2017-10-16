#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 16:16:58 2017

@author: bhl
"""
balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02

def paydebt(b, annualIR, monthlyPR, month):
    """
    balance : intial credit card balance, type float
    annualIR: annual interest rate, type float
    monthlyPR: monthly payment rate, type float
    month: month for paying debt, type int >= 0
    """
    if month == 0:
        b = b
        return  b
    else:
        return ((annualIR / 12 + 1) * paydebt(b * (1 - monthlyPR), annualIR, monthlyPR, month - 1))
remaining_b = 0
months = 12
remaining_b = round(paydebt(balance, annualInterestRate, monthlyPaymentRate, months), 2) 
print("Remaining balance: ",remaining_b )