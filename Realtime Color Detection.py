import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10, 100)
def empty(a):
    pass
cv2.namedWindow("HSVTrackbar")
cv2.resizeWindow("HSVTrackbar", 640, 240)
cv2.createTrackbar("HUE Min", "HSVTrackbar",0,179,empty)
cv2.createTrackbar("HUE Max","HSVTrackbar",179,179,empty)
cv2.createTrackbar("SAT Min","HSVTrackbar",0,255,empty)
cv2.createTrackbar("SAT Max","HSVTrackbar",255,255,empty)
cv2.createTrackbar("VALUE Min","HSVTrackbar",0,255,empty)
cv2.createTrackbar("VALUE Max","HSVTrackbar",255,255,empty)



while True:
    success, img=cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("HUE Min","HSVTrackbar")
    h_max = cv2.getTrackbarPos("HUE Max", "HSVTrackbar")
    s_min = cv2.getTrackbarPos("SAT Min", "HSVTrackbar")
    s_max = cv2.getTrackbarPos("SAT Max", "HSVTrackbar")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSVTrackbar")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSVTrackbar")

    lower= np.array([h_min,s_min,v_min] )
    upper= np.array([h_max,s_max,v_max])
    mask= cv2.inRange(imgHSV, lower, upper)
    result= cv2.bitwise_and(img,img, mask= mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack=np.hstack([img,mask,result])




    # cv2.imshow('video', img)
    # cv2.imshow("HSV", imgHSV)
    # cv2.imshow("Mask", mask )
    # cv2.imshow("Result", result)

    cv2.imshow("Hor_Stack", hStack)


    if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()






