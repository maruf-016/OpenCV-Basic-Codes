import cv2
cap =cv2.VideoCapture(0)

#tracker = cv2.TrackerBoosting_create()
#tracker = cv2.TrackerMIL_create()
#tracker = cv2.TrackerKCF_create()
#tracker = cv2.TrackerTLD_create()
#tracker = cv2.TrackerMedianFlow_create()
#tracker = cv2.TrackerCSRT_create()
tracker = cv2.TrackerMOSSE_create()
success, img =cap.read()
Bbox=cv2.selectROI("Tracking", img, False)
tracker.init(img,Bbox)
def drawbox(imgg,Bbox):
    x,y,w,h = int(Bbox[0]),int(Bbox[1]),int(Bbox[2]),int(Bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)), (0,0,255), 2,1)
    cv2.putText(img, "Tracking", (90, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255,0), 2)

while True:
    timer=cv2.getTickCount()
    success, img =cap.read()
    success, Bbox= tracker.update(img)
    if success:
        drawbox(img, Bbox)
    else:
        cv2.putText(img, "Lost", (90,90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img, str(int(fps)),(75,75),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1 )

    cv2.imshow("Tracking", img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
