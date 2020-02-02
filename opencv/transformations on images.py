import cv2
import numpy as np
img=cv2.imread('images.jpg')

#TRANSFORMATION-SCALING OF IMAGES

#cv2.resize(image to be transformed, none, scaling in x axis, scaling in y axis, inter polation)
#inter polation methods:
#INTER_LINEAR - 
#INTER_NEAREST - 
#INTER_AREA - use this to shrink the image
#INTER_CUBIC - use this to zoom the image(for 4x4 neighbourhood)
#INTER_LANCZ0S4 - use this to zoom the image(for 8x8 neighbourhood)



#L_output=cv2.resize(img,None,fx=1,fy=1.5,interpolation=cv2.INTER_LINEAR)
#A_output=cv2.resize(img,None,fx=1,fy=1.5,interpolation=cv2.INTER_AREA)
cv2.imshow('original',img)
#cv2.imshow('L transformed',L_output)
#cv2.imshow('A transformed',A_output)

#TRANSLATION-SHIFTING OF IMAGES

#for any geometric transformation on image we use cv2.warpAffine()
#in-order to perform a transformation we have to create a transformation matrix


#creation of transformation matrix

rows, columns, channels= img.shape
print(rows,columns)
##print(rows,columns)
##T=np.float32([[1,0,50],[0,1,50]])
##output=cv2.warpAffine(img,T,(columns,rows))
##print(output.shape)
##cv2.imshow('transformed',output)

###ROTATION
##T=cv2.getRotationMatrix2D((columns/2,rows/2), 45, 0.5)#gives a 2D transformation matrix as output((originpoint of the rotation),angle of rotation, scaling)
###(columns/2,rows/2) means centeral axis of rotation
##print(T)
##output=cv2.warpAffine(img,T,(columns,rows))
##print(output.shape)
##cv2.imshow('transformed',output)


#Affine Transformation- parallelism between lines in both original image and output image is preserved

#cv2.getAffineTransform()- calculates the transform matrix
#cv2.warpAffine()

#in order to calculate the affine transform matrix we need set of 2 points
#1st set of points- corresponds to those in the original image
#2nd set of points- corresponds to how the transformation is going to happen
##p1->o1
##p2->o2
##p3->o3

#as we need 3 pts to define a plane each set of points have 3 points and these 3 points should be non collinear


##point1=np.float32([[100,100],[300,100],[100,300]])
##point2=np.float32([[200,100],[400,150],[400,300]])
##A=cv2.getAffineTransform(point1,point2)
##output=cv2.warpAffine(img,A,(columns,rows))
##cv2.imshow('transformed',output)

#perspective transformation-

#cv2.getPerspectiveTransform()- calculates the transform matrix
#cv2.warpPerspective()

#here 4 points of 2 sets are required

point1=np.float32([[0,0],[225,0],[255,225],[0,225]])#corners of the image
point2=np.float32([[20,0],[120,0],[120,120],[20,120]])
A=cv2.getPerspectiveTransform(point1,point2)
output=cv2.warpPerspective(img,A,(columns,rows))
cv2.imshow('transformed',output)















