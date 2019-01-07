#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:33:00 2019

@author: abhijithneilabraham
"""
'''
I am gonna modify A* as per my own rules
'''

def distance(x,y):
    return ((x**2)+(y**2))**.5
print(distance(3,4))
def __init__(self, parent=None, position=None):
    self.parent = parent
    self.position = position

    self.g = 0
    self.h = 0
    self.f = 0

def __eq__(self, other):
    return self.position == other.position
