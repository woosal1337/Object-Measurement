import cv2
import numpy
import utlis


webcam = False

path = "data/1.jpeg"

cap = cv2.VideoCapture(0)
cap.set(10,160)
cap.set(3, 1920)
cap.set(4, 1080)

while True:
    if webcam:
        success, img = cap.read()
    else:
        img = cv2.imread(path)
        img = cv2.resize(img, (0,0), None, 0.5,0.5)

    utlis.getContours(img, showCannny=True)


    cv2.imshow("Original", img)
    cv2.waitKey(1)