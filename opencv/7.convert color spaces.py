import cv2
frame=cv2.imread('images.jpg')
gray = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
cv2.imshow('frame',gray)
