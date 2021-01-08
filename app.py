import cv2
import numpy as np

lowerBound = np.array([33, 80, 40])
upperBound = np.array([102, 255, 255])

cam = cv2.VideoCapture(0)

while True:
    ret, img = cam.read()
    img = cv2.resize(img, (340, 220))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(imgHSV, lowerBound, upperBound)
    edges = cv2.Canny(mask, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 40)

    if lines is not None:
        for rho, theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * a)
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * a)
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
            try:
                slope = (y2 - y1)/(x2 - x1)
                print((np.arctan(slope)*100))
            except ZeroDivisionError:
                print("90 degree or 270 degree")

    cv2.imshow("lines", edges)
    cv2.imshow("mask", mask)
    cv2.imshow("cam", img)
    cv2.waitKey(10)
