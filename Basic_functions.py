import cv2
import numpy as np
kernel=np.ones((5,5), np.uint8)
img= cv2.imread('H:\My Projects\OpenCV\lena.jpg')
imgGray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur= cv2.GaussianBlur(img,(7,7),0)
imgCanny=cv2.Canny(img,100,100)
imgDialation=cv2.dilate(imgCanny,kernel, iterations=1)
imgEroded= cv2.erode(imgDialation,kernel,iterations=1)
cv2.imshow("Original", img)
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Dilation", imgDialation)
cv2.imshow("Erode", imgEroded)
cv2.waitKey(0)

