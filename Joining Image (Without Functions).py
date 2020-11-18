import cv2
import numpy as np
img1= cv2.imread("H:\My Projects\OpenCV\lambo.jpg",0)
img2=cv2.imread("H:\My Projects\OpenCV\lena.jpg")
img1=cv2.resize(img1,(330,220),None, 0.5, 0.5)
img2=cv2.resize(img2,(330,220),None, 0.5, 0.5)
img1=cv2.cvtColor(img1,cv2.COLOR_GRAY2BGR)
print(img1.shape)
print(img2.shape)

hor=np.hstack((img1,img2))

cv2.imshow("H", hor)
cv2.waitKey(0)