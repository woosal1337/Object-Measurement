import cv2
import numpy as np

def getContours(img, cThr=[100,100], showCannny=False):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
    imgCanny = cv2.Canny(imgBlur, cThr[0], cThr[1])
    if showCannny:
        cv2.imshow("Canny", imgCanny)