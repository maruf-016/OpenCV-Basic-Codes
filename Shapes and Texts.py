import cv2
import numpy as np
img= np.zeros((512,512, 3), np.uint8)
img[:]= 255,155,160
cv2.line(img,(0,0),(300,300),(0,0,230),5)
cv2.rectangle(img,(250,250),(350,350),(0,0,150),2)
cv2.circle(img,(350,150),50,(255,150,0),2)
cv2.putText(img,"Hello", (300,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,0),1)
print(img)
print(img.shape)
cv2.imshow("image", img)
cv2.waitKey(0)

