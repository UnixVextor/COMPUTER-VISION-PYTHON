import cv2 
import numpy as np

# load an clor image in grayscale
img = cv2.imread("image/Tesla.jpg",0)

# set the window size mode
cv2.namedWindow('Image',cv2.WINDOW_NORMAL)  

#display window
cv2.imshow("Image",img)
#wait key from window => 0 is wait forever
cv2.waitKey(0)
#close specific window 
cv2.destroyWindow(img)
