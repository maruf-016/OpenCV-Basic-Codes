import cv2
import numpy as np
img= cv2.imread("H:\My Projects\OpenCV\card.png")
width,height= 250,350
pts1=np.float32([[9,152],[234,4],[255,493],[488,311]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOut=cv2.warpPerspective(img,matrix,(width,height))
for i in range (0,4):
    cv2.circle(img,(pts1[i][0],pts1[i][1]),5,(0,0,255),cv2.FILLED)
    
cv2.imshow("Warp", imgOut)
cv2.imshow("Original", img)
cv2.waitKey(0)