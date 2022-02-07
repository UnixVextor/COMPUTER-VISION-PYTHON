import cv2
import numpy as np

img = cv2.imread("image/Tesla.jpg",0)
cv2.imshow("Tesla",img)

k = cv2.waitKey(0)   # another way cv2.waitkey(0) & 0xFF
if k == 27:                 # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):         # wait for s to save and exit
    cv2.imwrite("output",img)
    cv2.destroyAllWindows()