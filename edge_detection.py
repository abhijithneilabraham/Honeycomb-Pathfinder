#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 01:31:56 2019

@author: abhijithneilabraham
"""
import numpy as np
import cv2 as cv
img = cv.imread('new.png',0)
edges = cv.Canny(img,100,200)

