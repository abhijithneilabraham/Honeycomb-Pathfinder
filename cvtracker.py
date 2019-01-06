import numpy as np
import cv2 
im=cv2.imread('new.png')
imgray = cv2.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()