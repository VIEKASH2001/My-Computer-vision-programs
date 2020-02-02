import numpy as np
import cv2
import cv2.aruco as aruco
frame=cv2.imread("0.jpeg")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)
parameters =  aruco.DetectorParameters_create()
corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
print(rejectedImgPoints)
gray = aruco.drawDetectedMarkers(gray, corners)
cv2.imshow('frame',gray)
    

