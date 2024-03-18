import cv2


img=cv2.imread('photos/imgg.jpeg')

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("gr",gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows