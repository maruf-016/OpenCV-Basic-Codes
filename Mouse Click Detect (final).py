import cv2
import numpy as np

circles=np.zeros((4,2), np.int)
counter=0

def mousepoints(events,x,y,flags,params):
    global counter
    if events==cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        circles[counter]=x,y
        counter=counter+1
        print(circles)
img = cv2.imread("H:\My Projects\OpenCV\card.png")
while True:
    if counter==4:
        width, height = 250, 350
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOut = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("Warp", imgOut)


    for i in range(0, 4):
        cv2.circle(img, (circles[i][0],  circles[i][1]), 5, (0, 255,0), cv2.FILLED)


    cv2.imshow("Original", img)
    cv2.setMouseCallback("Original", mousepoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break