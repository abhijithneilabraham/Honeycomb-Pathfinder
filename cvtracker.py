import numpy as np
import cv2 
from astar_algorithm import astar


def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:#sadly,in my mac,the event mouseclick doesnt work.so,please feel free to change this.
        cv2.circle(img,(x,y),1,(255,0,0),-1)
        print(x,y)
        
img=cv2.imread('honeycomb.jpg')#read the image
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#to greyscale conversion
print(contours)
gray = np.float32(imgray)#converting to float32 for giving input to cornerharris
dst = cv2.cornerHarris(gray,2,3,0.04)#cornerharris detects the intensity changes in all direction and thus finds a corner
#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]
edges = cv2.Canny(img,100,200)#cannyedge function for detecting the edges . 100 and 200 are threshold values
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle) 
start = (120, 90)
end = (428, 90)

path = astar(contours, start, end)
print(path)

    
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

