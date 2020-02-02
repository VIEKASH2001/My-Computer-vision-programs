import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(1):

    # Take each frame
    _, frame = cap.read()
    cv2.imshow('frame', frame)
    k = cv2.waitKey(5)
    if k==27:
        cv2.imwrite("F:\capture.png",frame)
        break


gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("thresh",thresh)

image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = cv2.drawContours(frame, contours, -1,(0,255,0), 3)
cv2.imshow('cnt',cnt)

# create hull array for convex hull points
hull = []
 
# calculate points for each contour
for i in range(len(contours)):
    # creating convex hull object for each contour
    hull.append(cv2.convexHull(contours[i], False))

# create an empty black image
drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
 
# draw contours and hull points
for i in range(len(contours)):
    color_contours = (0, 255, 0) # green - color for contours
    color = (255, 0, 0) # blue - color for convex hull
    # draw ith contour
    cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
    # draw ith convex hull object
    cv2.drawContours(drawing, hull, i, color, 1, 8)

defects = cv2.convexityDefects(cnt,drawing)
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(frame,start,end,[0,255,0],2)
    cv2.circle(frame,far,5,[0,0,255],-1)

cv2.imshow('img',frame)
