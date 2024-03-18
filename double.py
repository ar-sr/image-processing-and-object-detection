import cv2
import numpy as np


img=cv2.imread('photos/test.jpg')
re_img=cv2.resize(img,(300,700))
h=np.hstack((re_img,re_img))

cv2.imshow("image",h)
cv2.waitKey(0)
cv2.destroyAllWindows()



