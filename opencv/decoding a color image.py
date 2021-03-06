import cv2

#to display the image
img=cv2.imread('images.jpg')
cv2.imshow("image",img)

#to see what is inside the image array
print(img)#give an array of the pixels of image

print(type(img))#gives the data type of the image
#numpy.ndarray means: N dimensional arrays, numppy = Numerical Python

print(img.dtype)#data type of constituent elements of the image
#unit8 means: unsigned integer 8-bits
#lowest value of unit8= 00000000(binary) or 0x00(hex) or 0(decimal)
#highest value of unit 8=11111111(binary) or 0xFF(hex) or 255(decimal)

print(img.shape)#gives the resolution and no.of color channels of images of images
#gives output: (225, 225, 3)
#means: 225 x 225 is the resolution and 3 is the number of color channels in each tuple

print(img.ndim)#returns the number of dimensions
#output=3 (3D ARRAY)
#1st dimension= 225 (height)
#2nd dimension= 225 (width)
#3rd dimension= 3 (no.of color channels)
#note: in grayscale image and in B/W image no,of colorspaces =1 , so the no.of dimensions =2

print(img.size)# size = 225x225x3 = 151875 bytes= 151KB

cv2.waitKey(0)

