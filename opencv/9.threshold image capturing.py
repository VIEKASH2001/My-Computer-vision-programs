import cv2

cap = cv2.VideoCapture(0)
# Capture frame-by-frame
ret, frame = cap.read()
# Display the resulting frame
cv2.imshow("Frame",frame)

# convert the resized image to grayscale, blur it slightly,
# and threshold it
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("thresh",thresh)

#find contours in the thresholded image and initialize the shape detector
image, cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
im = cv2.drawContours(frame, cnts, -1,(0,255,0), 3)
cv2.imshow("cnt",im)
cv2.waitKey(0)
