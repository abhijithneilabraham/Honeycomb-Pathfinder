#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 12:41:19 2019

@author: abhijithneilabraham
"""

import numpy as np
import cv2 
from modified_astar import astar


def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:#sadly,in my mac,the event mouseclick doesnt work.so,please feel free to change this.
        cv2.circle(img,(x,y),1,(255,0,0),-1)
        print(x,y)
        
img=cv2.imread('square.jpeg')#read the image
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#to greyscale conversion

gray = np.float32(imgray)#converting to float32 for giving input to cornerharris
dst = cv2.cornerHarris(gray,2,3,0.04)#cornerharris detects the intensity changes in all direction and thus finds a corner
dst = cv2.dilate(dst,None)
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)

corners=[]
# define the criteria to stop and refine the corners
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners=cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)



img[dst>0.1*dst.max()]=[0,0,255]

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle) 
#result is dilated for marking the corners, not important

# Threshold for an optimal value, it may vary depending on the image.

start = ( 99.46604 , 98.886505)
end = (132.51556,  32.676155)

path = astar(contours,corners, start, end)
print(path)

