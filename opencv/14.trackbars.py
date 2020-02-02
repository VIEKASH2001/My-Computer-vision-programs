import cv2
import numpy as np

def emptyfunction(X):#this is how we create an empty function, it should have ny arguement
    pass

image=np.zeros((512,512,3),np.uint8)
windowname="Tracbar window"
cv2.namedWindow(windowname)#this is to create a window with a name and this typw of window is usually created when you want to control the screen
cv2.createTrackbar('B',windowname,0,255,emptyfunction)#(<track bar name>,<windowname>,minimum value of color,maximum value of color,any fumction to perform the prefered action(as here no need to perform any action just create some empty function))
cv2.createTrackbar('G',windowname,0,255,emptyfunction)
cv2.createTrackbar('R',windowname,0,255,emptyfunction)
while True:
    blue=cv2.getTrackbarPos('B',windowname)#this function returns the current value of the trackbar
    green=cv2.getTrackbarPos('G',windowname)
    red=cv2.getTrackbarPos('R',windowname)
    image[:]=[blue,green,red]#variable[:] means all the elements in that dimension of the array. so by doing this we are defining color values to each of the 3 pixels. thy have to be in B G R order
    print(blue,green,red)
    cv2.imshow(windowname,image)
    if cv2.waitKey(1)==27:
        break
   
cv2.destroyAllWindows()
