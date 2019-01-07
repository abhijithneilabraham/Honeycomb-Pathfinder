#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 01:31:56 2019

@author: abhijithneilabraham
"""
import numpy as np
import cv2 
img = cv2.imread('new.png',0)
edges = cv2.Canny(img,100,200)
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(img,(x,y),1,(255,0,0),-1)

# Create a black image, a window and bind the function to window

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
