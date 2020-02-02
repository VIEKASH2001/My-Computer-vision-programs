import cv2
cap = cv2.VideoCapture(0)
# Capture frame-by-frame
ret, frame = cap.read()
# Display the resulting frame
cv2.imshow("Frame",frame)
