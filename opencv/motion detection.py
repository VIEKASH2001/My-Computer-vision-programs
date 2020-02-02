import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    _, frame1 = cap.read()
    _, frame2 = cap.read()
    difference = cv2.absdiff(frame1, frame2)
    cv2.imshow("Orig", difference)
    grey = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (5, 5), 0)
    _, thresh = cv2.threshold( blur, 15, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, np.ones((3, 3), np.uint8), iterations=15 )
    eroded = cv2.erode(dilated, np.ones((3, 3), np.uint8), iterations=15 )
    contours,_ = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame1, contours, -1, (0, 0, 255), 2)
    cv2.imshow("Original", frame2)
    cv2.imshow("Output", frame1)
    if cv2.waitKey(1) == 27:
            break
    


        
cv2.destroyAllWindows()
cap.release()

