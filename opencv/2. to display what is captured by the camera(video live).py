import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(1):

    # Take each frame
    _, frame = cap.read()
    cv2.imshow('frame', frame)
    k = cv2.waitKey(5)
    if k==27:
        break

cv2.imwrite("F:\capture.png",frame)
# Select ROI
r = cv2.selectROI(frame)
#Crop image
imCrop = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
# Display cropped image
cv2.imshow("Image", imCrop)
print(imCrop.shape)

