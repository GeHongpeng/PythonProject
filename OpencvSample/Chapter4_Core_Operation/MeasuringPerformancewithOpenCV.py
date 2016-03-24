# _*_ coding= utf-8 _*_

import cv2
import numpy as np

img1 = cv2.imread("./data/Penguins.jpg")

e1 = cv2.getTickCount()
for i in xrange(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)

e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print t  # Result I got is 2.10057293885 seconds
"""
You can do the same with time module. Instead of cv2.getTickCount, use time.time() function.
Then take the difference of two times.
"""
