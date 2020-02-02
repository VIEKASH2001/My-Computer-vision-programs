import cv2
import numpy as np
cap = cv2.VideoCapture(0)
kernel = np.ones((5,5),np.uint8)
object_width=3#in cm
distance=15#from camera in cm(for measuring focal_length)
#focal_length = (pixel_width x  distance) / object_width
focal_length=540#measured
while(1):
    cmin=640
    cmax=0
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blurred = cv2.GaussianBlur(hsv, (5, 5), 0)
    lower_green = np.array([50,160,40])
    upper_green = np.array([80,255,255])
    greenmask = cv2.inRange(blurred, lower_green, upper_green)
    gerosion = cv2.erode(greenmask,kernel,iterations = 4)
    gdilation = cv2.dilate(gerosion,kernel,iterations = 4)
    contours,_ = cv2.findContours(gdilation , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
    if(contours!= []):
        length=len(contours[0])
        for i in range(length):
             if(contours[0][i][0][0]<cmin):
                 cmin=contours[0][i][0][0]
             if(contours[0][i][0][0]>cmax):
                 cmax=contours[0][i][0][0]
        pixel_width=cmax-cmin
        Z_distance = int((object_width*focal_length)/pixel_width)
        print(Z_distance)
    cv2.drawContours(frame, contours, -1, (0,0,255), 3)
    cv2.imshow("cont",frame)
    k = cv2.waitKey(5)
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
