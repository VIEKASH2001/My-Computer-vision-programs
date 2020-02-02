import cv2
import numpy as np

image =np.zeros((512,512,3),np.uint8)
image_to_show = np.copy(image)
i=0
windowname="Paint Window"
finish = False
cv2.namedWindow(windowname)

def draw_circle(event,x,y,flags,parameters):
     if(event==cv2.EVENT_LBUTTONDOWN):#left button single click
               cv2.circle(image_to_show,(x,y),40,(255,255,0),-1)
while not finish:
    cv2.imshow(windowname, image_to_show)
    key = cv2.waitKey(0)
    if key == ord('C'):
       cv2.setMouseCallback(windowname,draw_circle)
     
    elif key == ord('l'):
        cv2.line(image_to_show, rand_pt(), rand_pt(), (0, 255, 0), 3)
    elif key == ord('r'):
        cv2.rectangle(image_to_show, rand_pt(), rand_pt(), (0, 0, 255), 3)
    elif key == ord('e'):
        cv2.ellipse(image_to_show, rand_pt(), rand_pt(), random.randrange(360), 0, 360, (255, 255, 0), 3)
    elif key == ord('t'):
        cv2.putText(image_to_show, 'OpenCV', rand_pt(), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    elif key == ord('S'):  
        text = "paint_"+str(i) 
        cv2.imwrite(text,image)
        i+=1
    elif key == ord('E'):
        image_to_show = np.copy(image)
    elif key == 27:
        finish = True
    
