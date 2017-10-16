#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:55:47 2017

@author: bhll
"""

print("Please think of a number between 0 and 100!")

# At the start the highest the number could be is 100 and the lowest is 0.
hi = 100
lo = 0
guessed = False

while not guessed:
    guess_num = (hi + lo) // 2
    print("Is your secret number " + str(guess_num)+ "?")
    eva_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if eva_input == "c":
        print("Game over. Your secret number was: ", guess_num)
        guessed = True
    elif eva_input == "h":
        hi = guess_num
    elif eva_input == "l":
        lo = guess_num
    else:
        print("Sorry, I did not understand your input.")
