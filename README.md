# ColourSegmentation

## NAME

Akshath Dubey 

## CONTACT 

GitHub: https://github.com/akshathdubey

Email: dubeyakshath19@gmail.com 

## TASK 

Video feed captured by the web camera and print the angle of its heading with respect to the vertical axis of the image. 

## PROGRAM 

**Importing modules.** 
```
import cv2 
import numpy as np 
```

**Setting lower and upper boundaries for masking.**
```
lowerBound = np.array([1, 50, 20]) 
upperBound = np.array([4, 255, 255]) 
```

**Getting video feed from camera.**
```
cam = cv2.VideoCapture(0)
while True: 

# Read Camera 
ret, img = cam.read() 
```

**Resizing the input.**
```
# Resize 
img = cv2.resize(img, (320, 180)) 
```

**Blurring the image is useful for removing noise. We give the size of the kernel I.e., its width and height which is always an odd number.**
```
# Blur 
Blur = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT) 
```

**Now we are converting the blurred image to HSV for colour segmentation.**
```
# Convert to HSV 
imgHSV = cv2.cvtColor(Blur, cv2.COLOR_BGR2HSV) 
```

**We have defined the lower and upper boundaries for HSV, now the inRange() will make all pixels not lying in the set boundaries black and pixels lying inside the set boundaries will become white.**
```
# Mask
mask = cv2.inRange(imgHSV, lowerBound, upperBound) 
```

**To remove noise, we use erosion and dilation. In erosion a kernel of a size we set (again, odd number) analyzes the whole image and if any pixel under the kernel area is black then the whole kernel area is turned black.**
```
# Erosion
eros = cv2.erode(mask, (3, 3), iterations=3) 
```

**After erosion the noises are removed. Now, we again make a kernel analyze the image and if any pixel under the kernel area is white then the whole kernel is turned white. After erosion removes the noise, we use dilation to restore the shape of the object.**
```
# Dilating 
dilation = cv2.dilate(eros, (7, 7), iterations=1) 
```

**Now we find the contours using findContours() function. It gives us the boundary of the object.**
```
# Find the contours 
contours, _ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) 
```

**Now, we will run a for loop to get the vertices from the contour.**
```
# For each contour approximate the curve 
for cnt in contours: 
```

**contourArea will return the area of contour which we will use to eliminate noise**
```
area = cv2.contourArea(cnt) 
if area > 50: 
```

**The function approxPolyDP() approximates the contour giving us a set of coordinates of vertices through which we can determine the shape.**
```
epsilon = 0.01 * cv2.arcLength(cnt, True) 
approx = cv2.approxPolyDP(cnt, epsilon, True) 
```

**Now, we will check if the number of coordinates in the approximated contour is 7.**
```
if len(approx) == 7: 
```

**drawContours() draws the shape whose boundary points we give as argument. The first argument is the image where we want to draw the contours, second argument is the set of boundary points, third argument is –1 because it will give us all the contours in the image, fourth is the colour of contour and fifth is the thickness of contour.**
```
# Draw contours 
cv2.drawContours(img, [approx], -1, (0, 0, 255), 1) 
```

**Now we show the mask and the original image.**
```
cv2.imshow("mask", dilation) 
cv2.imshow("cam", img) 
cv2.waitKey(10)
```
