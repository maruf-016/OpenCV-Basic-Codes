import cv2
import numpy as np
img=cv2.imread("H:\My Projects\OpenCV\lambo.jpg")
print(img.shape)
imgResize= cv2.resize(img,(200,300))
print(imgResize.shape)
imgCropped= img[0:200,200:500]
cv2.imshow("Original", img)
cv2.imshow("Resize",imgResize)
cv2.imshow("Cropped", imgCropped)
cv2.waitKey(0)
