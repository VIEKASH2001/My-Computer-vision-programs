import cv2
image = cv2.imread("2.jpg")

# we need to keep in mind aspect ratio so the image does
# not look skewed or distorted -- therefore, we calculate
# the ratio of the new image to the old image

#do the below calculation to maintain the aspect ratio
#r = 225.0/ image.shape[1] #shape[1] means the width
#dim = (225, int(image.shape[0] * r))#shape[0] means the height



#if you want the image resolution to be as per ypur wish irrescpectiove of the aspect ratio then do directly
dim=(499,636) 
# perform the actual resizing of the image and show it
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)#cv2.resize(image,new resolution,interpolation = cv2.INTER_AREA)
cv2.imshow("n2", resized)
print(resized.shape)
cv2.imwrite('n2.jpg',resized)
cv2.waitKey(0)
