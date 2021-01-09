import cv2
import numpy as np

lowerBound = np.array([175, 50, 20])
upperBound = np.array([180, 255, 255])

lowerBound2 = np.array([0, 50, 20])
upperBound2 = np.array([2, 255, 255])

cam = cv2.VideoCapture(0)

while True:
    # Read Camera
    ret, img = cam.read()
    # Resize
    img = cv2.resize(img, (340, 220))
    # Convert to HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Mask 1
    mask1 = cv2.inRange(imgHSV, lowerBound, upperBound)
    # Mask 2
    mask2 = cv2.inRange(imgHSV, lowerBound2, upperBound2)
    # Final mask
    mask = mask1 + mask2
    # Convert to binary image by thresholding
    _, threshold = cv2.threshold(mask, 60, 255, cv2.THRESH_BINARY_INV)
    # Find the contours
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # For each contour approximate the curve
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            epsilon = 0.01 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)

            coord = approx
            # Draw contours
            cv2.drawContours(img, [approx], -1, (0, 0, 255), 1)

            if len(approx) == 7:

                try:
                    x1, y1 = coord[0][0]
                    x2, y2 = coord[0][1]
                    x3, y3 = coord[0][2]
                    x4, y4 = coord[0][3]
                    x5, y5 = coord[0][4]
                    x6, y6 = coord[0][5]
                    x7, y7 = coord[0][6]

                    m = []

                    m[0] = (y2 - y1)/(x2 - x1)
                    m[1] = (y3 - y2)/(x3 - x2)
                    m[2] = (y4 - y3)/(x4 - x3)
                    m[3] = (y5 - y4)/(x5 - x4)
                    m[4] = (y6 - y5)/(x6 - x5)
                    m[5] = (y7 - y6)/(x7 - x6)
                    m[6] = (y1 - y7)/(x1 - x7)

                    i = 0
                    for i in m:
                        if m[i] == 1:
                            if m[i+2] == 1:
                                try:
                                    print(np.arctan(m[i])*100 + np.arctan(m[i+2])*100)

                                except ZeroDivisionError:
                                    print("90 degree or 270 degree")

                except IndexError:
                    print("\n")

    cv2.imshow("mask", mask)
    cv2.imshow("cam", img)
    cv2.waitKey(10)
