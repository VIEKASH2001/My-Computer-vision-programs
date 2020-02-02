import cv2
img1=cv2.imread('resized.jpg')
img2=cv2.imread('images.jpg')

#bitwise operations happen pixel wise
#each pixel intensity is converted to binary digit and is operated

img3=cv2.bitwise_not(img1)
cv2.imshow('not',img3)
img4=cv2.bitwise_and(img1,img2)
cv2.imshow('and',img4)
img5=cv2.bitwise_or(img1,img2)
cv2.imshow('or',img5)
img6=cv2.bitwise_xor(img1,img2)
cv2.imshow('xor',img6)


