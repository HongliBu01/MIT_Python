#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 17:03:58 2017

@author: bhl
"""
import math

def polysum(n, s):
    """
    n : number of sides in a regular polygon 
    s : length of each side in the polygon 
    sum the area and square of the perimeter of the regular polygon
    """
    return round((0.25*n*s**2/(math.tan(math.pi/n)) + (n*s)**2), 4)
