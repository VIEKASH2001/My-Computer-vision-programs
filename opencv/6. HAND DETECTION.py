import cv2
import numpy as np
frame= cv2.imread("hand.jpg")
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
kernel = np.ones((3,3),np.uint8)
# define range of skin color in HSV
lower_skin = np.array([0,30,70], dtype=np.uint8)
upper_skin = np.array([20,255,255], dtype=np.uint8)
mask = cv2.inRange(hsv, lower_skin, upper_skin)
mask = cv2.dilate(mask,kernel,iterations = 4)
mask = cv2.GaussianBlur(mask,(5,5),100)
#find contours
_, contours,hierarchy= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
im = cv2.drawContours(frame, contours, -1,(0,255,0), 3)
cv2.imshow('Contour',im)
cv2.imshow('Mask',mask)
cv2.waitKey(0)
