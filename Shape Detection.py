import cv2
import numpy as np
import imgstack

def empty(a):
    pass
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(1)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 255,255,empty)
cv2.createTrackbar("Threshold2","Parameters", 183,255,empty)
cv2.createTrackbar("Area","Parameters",5000,30000,empty)

def getContours(img, imgCont):
    contours, hierarchy= cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        areaMin=cv2.getTrackbarPos("Area","Parameters")
        if area>areaMin:
           cv2.drawContours(imgCont,cnt,-1, (0,0,255),5)
           peri=cv2.arcLength(cnt,True)
           approx=cv2.approxPolyDP(cnt, 0.02*peri, True)
           print(approx)
           x,y,w,h = cv2.boundingRect(approx)
           cv2.rectangle(imgCont,(x,y),(x+w,y+h),(255,0,0),5)
           cv2.putText(imgCont, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, .7,
                       (0, 255, 0), 2)
           cv2.putText(imgCont, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                       (0, 255, 0), 2)











while True:
    success, img = cap.read()
    imgCont=img.copy()
    imgBlur= cv2.GaussianBlur(img, (7,7), 1)
    imgGray= cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    th1=cv2.getTrackbarPos("Threshold1", "Parameters")
    th2=cv2.getTrackbarPos("Threshold2", "Parameters")
    imgCanny=cv2.Canny(imgGray,th1,th2)
    kernel=np.ones((5,5))
    imgDil=cv2.dilate(imgCanny,kernel,iterations=1)
    getContours(imgDil,imgCont)




    imgStack = imgstack.stackImages(0.8, ([img, imgGray,imgCanny],
                                          [imgDil,imgCont,imgCont]))
    cv2.imshow("Result", imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

