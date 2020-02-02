import cv2
import numpy as np
cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #our colour is bgr but we want to convert it to hsv for easv color selection
    # now choosing the range of blue that u want to display, here we chose hsv because we can shoose the range of colors,here the range is in an array and the lower and upper blue indicates the blue parts
    lower_blue = np.array([100,60,50]) # this lower and upper space values are pre known,by modyfing this by a bit we can get other colors also
    upper_blue = np.array([130,255,255])
    #Creating a smooth/mask where the values in the range are made 255 others are made 0
    mask = cv2.inRange(hsv , lower_blue, upper_blue)
    #Creating a filter/res where the values in the range a
    res = cv2.bitwise_and(frame, frame,mask = mask)
    cv2.imshow('Frame',frame) #shows the actual frame
    cv2.imshow('Smooth', mask) #shows the converted frame where all the blue is converted to white and rest all is converted to black
    cv2.imshow('Filter', res) # shows the frame in which there is only blue colour where rest all is made black
    cv2.waitKey(1)
