# _*_ coding= utf-8 _*_
import cv2
import numpy as np

"""
Changing Color-space

For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255].
Different softwares use different scales.
So if you are comparing OpenCV values with them, you need to normalize these ranges.
"""
# To get color flags
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print flags

"""
Object Tracking
"""
img = cv2.imread('./data/logo.png')

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('image', img)
cv2.imshow('mask', mask)
cv2.imshow('res', res)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Find HSV values to track
"""
green = np.uint8([[[0, 255, 0]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print hsv_green
