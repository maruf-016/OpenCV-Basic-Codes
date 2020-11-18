import cv2
import numpy as np

def mousepoints(events,x,y,flags,params):
    if events==cv2.EVENT_LBUTTONDOWN:
        print(x,y)

img= cv2.imread('H:\My Projects\OpenCV\lena.jpg')

cv2.imshow("Image",img)
cv2.setMouseCallback("Image", mousepoints)
cv2.waitKey(0)
