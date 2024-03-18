import cv2
import numpy as np


img=cv2.imread('photos/test.jpg')
blured=cv2.GaussianBlur(img,(15,15),2)

cv2.imshow("image",blured)
cv2.waitKey(0)
cv2.destroyAllWindows()