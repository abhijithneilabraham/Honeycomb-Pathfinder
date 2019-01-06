import numpy as np
import cv2 
img=cv2.imread('new.png')#read the image
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#to greyscale conversion
gray = np.float32(imgray)#converting to float32 for giving input to cornerharris
dst = cv2.cornerHarris(gray,2,3,0.04)#cornerharris detects the intensity changes in all direction and thus finds a corner
#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

edges = cv2.Canny(img,100,200)#cannyedge function for detecting the edges . 100 and 200 are threshold values

cv2.imshow('image',img)
cv2.waitKey(0)#wait for any keypress
cv2.destroyAllWindows()
