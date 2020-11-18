import cv2
img= cv2.imread('H:\My Projects\OpenCV\lena.jpg',0)

print(img)
cv2.imshow("Wind", img)
k= cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()
elif k== ord('s'):
    cv2.imwrite('H:\My Projects\OpenCV\lena2.jpg', img)

