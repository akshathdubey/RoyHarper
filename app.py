import cv2
import numpy as np

lowerBound = np.array([1, 50, 20])
upperBound = np.array([4, 255, 255])

cam = cv2.VideoCapture(0)

while True:
    # Read Camera
    ret, img = cam.read()

    # Resize
    img = cv2.resize(img, (320, 180))

    # Blur
    Blur = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)

    # Convert to HSV
    imgHSV = cv2.cvtColor(Blur, cv2.COLOR_BGR2HSV)

    # Mask
    mask = cv2.inRange(imgHSV, lowerBound, upperBound)

    # Erosion
    eros = cv2.erode(mask, (3, 3), iterations=3)

    # Dilating
    dilation = cv2.dilate(eros, (7, 7), iterations=1)

    # Find the contours
    contours, _ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # For each contour approximate the curve
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 50:
            epsilon = 0.01 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)

            if len(approx) == 7:
                # Draw contours
                cv2.drawContours(img, [approx], -1, (0, 0, 255), 1)

    cv2.imshow("mask", dilation)
    cv2.imshow("cam", img)
    cv2.waitKey(10)
