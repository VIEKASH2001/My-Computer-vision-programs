import cv2
img1=cv2.imread('resized.jpg')
img2=cv2.imread('images.jpg')


#scalar addition
sadd=img1+50 #adds 50 intensity to all the pixels and all the channels
cv2.imshow('sadd',sadd)

#2 images addition
add=img1+img2
cv2.imshow('add',add)



#same way do for all other operations
#-,*,/

