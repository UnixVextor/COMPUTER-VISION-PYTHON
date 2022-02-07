import matplotlib.pyplot as plt
import cv2
import numpy as np

# img = cv2.imread("image/Tesla.jpg",0)
# plt.imshow(img,cmap = 'gray',interpolation= 'bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick value on x and y axis
# plt.show()


img2 = cv2.imread("image/superman.jpg")
b,g,r = cv2.split(img2)
img3 = cv2.merge([r,g,b])
plt.subplot(121); plt.imshow(img2)
plt.subplot(122); plt.imshow(img3)
plt.show()
