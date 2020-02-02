import cv2
import numpy as np
#numpy is used to create our own images

img=np.zeros((512,512,3),np.uint8)#it creates a 3D array of all elements zero
#cv2.imshow("image",img) # this displays a black image


#drawing geometric shapes

#lines
img1=np.zeros((512,512,3),np.uint8)
cv2.line(img1,(0,99),(99,0),(255,0,0),2)# cv2.line(image,initial point,final point,color of a line given by a tuple/pixel,thickness)
cv2.imshow("line",img1)

#rectangle
img2=np.zeros((512,512,3),np.uint8)
cv2.rectangle(img2,(0,99),(99,0),(255,0,0),2)# cv2.rectangle(image,initial point of the diagonal,final point of the diagonal,color of a line given by a tuple/pixel,thickness)
cv2.imshow("rectangle",img2)

#circle
img3=np.zeros((512,512,3),np.uint8)
cv2.circle(img3,(60,60),10,(255,0,0),2)# cv2.circle(image,centre,radius,color of a line given by a tuple/pixel,thickness)
cv2.imshow("circle",img3)

#inorder to have a coloured shape put thickness =-1
#circular plate
img4=np.zeros((512,512,3),np.uint8)
cv2.circle(img4,(60,60),10,(255,0,0),-1)# cv2.circle(image,centre,radius,color of a line given by a tuple/pixel,thickness)
cv2.imshow("circle",img4)

#ellipse
img5=np.zeros((512,512,3),np.uint8)
cv2.ellipse(img5,(60,60),(50,20),45,0,360,(255,0,0),2)# cv2.ellipse(image,centre,axes(major,minor),angle,startAngle,endAngle,color of a line given by a tuple/pixel,thickness)
#angle: angle of major axis with x axis
#start angle and end angle are used to give full ellipse,half ellipse,quater ellipse,arbitary angled ellipse
cv2.imshow("ellipse",img5)

#polygons
img6=np.zeros((512,512,3),np.uint8)
points=np.array([[80,2],[125,40],[179,19],[230,5],[30,50]],np.int32)#5 points for a five sided polygon
points=points.reshape((-1,1,2))#reshaped into a 3D array
cv2.polylines(img6,[points],True,(255,0,0))#if third argument is False, you will get a polylines joining all the points, not a closed shape. 
cv2.imshow("polygon",img6)

#to write text
img7=np.zeros((512,512,3),np.uint8)
cv2.putText(img7,'test text',(100,100),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0))#cv2.putText(image,text,starting coordinate,font,size,color)
cv2.imshow("text",img7)



cv2.waitKey(0)

