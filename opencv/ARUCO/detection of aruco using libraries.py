import numpy as np
import cv2
import cv2.aruco as aruco
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_ARUCO_ORIGINAL)
    parameters =  aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    print(ids)
    gray = aruco.drawDetectedMarkers(gray, corners)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q') or ids==250:
        break
cv2.imwrite('frame1.jpg',frame)    
cap.release()
cv2.destroyAllWindows()
