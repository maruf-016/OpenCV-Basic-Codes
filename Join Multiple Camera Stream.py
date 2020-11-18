import cv2
import numpy as np
import imgstack


cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10, 100)
while (cap.isOpened()) :
    success, img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if success==True:

        kernel = np.ones((5, 5), np.uint8)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
        imgCanny = cv2.Canny(img, 100, 100)
        imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
        imgEroded = cv2.erode(imgDialation, kernel, iterations=1)




    video= imgstack.stackImages(0.5,([img,imgGray,imgBlur],[imgCanny,imgEroded,imgDialation]))
    cv2.imshow("StackedVideo", video)



    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break