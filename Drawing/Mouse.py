import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVEN' in i]  # list all avilable mouse events  
# print (events)

# mouse callback function 
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')  #arg have to same as arg -> setMouseCallBack()
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if(cv2.waitKey(20)) & 0xFF == 27:
        break
cv2.destroyAllWindows()