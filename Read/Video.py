import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while(True):
    # Capture frame by frame
    ret, fram = cap.read()

    # Our operation on the frame come here 
    gray = cv2.cvtColor(fram, cv2.COLOR_BGR2GRAY)

    # Display the resulting fram 
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everthing is done, release the capture
cap.release()
cv2.destroyAllWindows()