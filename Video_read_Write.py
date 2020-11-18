import cv2
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10, 100)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi', fourcc, 30.0, (640,480))
print(cap.isOpened())
while (cap.isOpened()) :
    success, img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if success==True:
        cv2.imshow('video', img)

        cv2.imshow('GV', gray)
        out.write(img)




        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break

    else:
        break


cap.release()
cv2.destroyAllWindows()