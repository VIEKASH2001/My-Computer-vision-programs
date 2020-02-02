import cv2
import numpy as np
windowname='drawing'
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow(windowname)
radius=10

def draw_circle(event,x,y,flags,parameters): #an action performing function
    #print("out")
    #print (flags)#0 if no event and 1 if event is made
    #in the below replace L with R to get right click functions and with M to get middle click functions
##    if(event==cv2.EVENT_LBUTTONDOWN):#left button single click
##        print("in 1")
##        print(parameters)
##        print (flags)
##        cv2.circle(img,(x,y),radius,(255,255,0),-1)
##    if(event==cv2.EVENT_LBUTTONDBLCLK):#left button double click
##        print("in 2")
##        cv2.circle(img,(x,y),40,(0,255,0),-1)    
##    if(event==cv2.EVENT_LBUTTONUP):#single click left button and while releasing the button only the image is formed
##        print("in 3")
##        cv2.circle(img,(x,y),40,(0,255,255),-1)    
##


    
    # replace L with R and M for other buttons  
    #if(event==cv2.EVENT_FLAG_LBUTTON):#left button single click
    #    cv2.circle(img,(x,y),40,(255,0,0),-1)




##    #by just moving the mouse without any clicks to draw
##    if(event==cv2.EVENT_MOUSEMOVE):#left button single click
##        print(x,y)
##        cv2.circle(img,(x,y),radius,(255,255,0),-1)
##
##    #by just rotating the mouse without any clicks to draw    
##    if(event==cv2.EVENT_MOUSEWHEEL):#left button double click
##        print(x,y)
##        cv2.circle(img,(x,y),40,(0,255,0),-1)

##EVENT_MOUSEWHEEL 	
##positive and negative values mean forward and backward scrolling, respectively.
##
##EVENT_MOUSEHWHEEL 	
##positive and negative values mean right and left scrolling, respectively.

##EVENT_FLAG_CTRLKEY 	
##indicates that CTRL Key is pressed.
##
##EVENT_FLAG_SHIFTKEY 	
##indicates that SHIFT Key is pressed.
##
##EVENT_FLAG_ALTKEY 	
##indicates that ALT Key is pressed.
    
   
        
cv2.setMouseCallback(windowname,draw_circle)#(windowname,any action performing function)
#this function is activated whenever we keep our mouse inside the window inspite of our click


while(True):
    cv2.imshow(windowname,img)
    if cv2.waitKey(20)==27:
        break

cv2.destroyAllWindows()    
