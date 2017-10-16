#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 21:16:14 2017

@author: bhl
"""
import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableletters = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        availableletters.remove(letter)
    return " ".join(availableletters)

