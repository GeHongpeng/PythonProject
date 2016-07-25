# _*_ coding= utf-8 _*_
import cv2
import numpy as np
import glob
from random import randint


def insideArea(r1, r2):
    x1, y1, w1, h1 = r1
    x2, y2, w2, h2 = r2

    if (x1 > x2) and (y1 > y2) and (x1 + w1 < x2 + w2) and (y1 + h1 < y2 + h2):
        return True
    else:
        return False


def insideXLine(r1, r2):
    x1, y1, w1, h1 = r1
    x2, y2, w2, h2 = r2

    if ((x1 <= x2) and (x1+w1 >= x2)) or ((x1 <= x2+w2) and (x1+w1 >= x2+w2)) or ((x1 > x2) and (x1+w1 < x2+w2)):
        print 'found: ', x1, x2, x1+w1, x2+w2
        return True
    else:
        return False


def wrap_digit(rect):
    x, y, w, h = rect
    padding = 5
    hcenter = x + w/2
    vcenter = y + h/2

    if h > w:
        w = h
        x = hcenter - (w/2)
    else:
        h = w
        y = vcenter - (h/2)

    return x-padding, y-padding, w+padding, h+padding


img = cv2.imread('./testdata/sample/sample6.jpg', 1)
bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bw = cv2.GaussianBlur(bw, (7, 7), 0)
ret, thbw = cv2.threshold(bw, 230, 255, cv2.THRESH_BINARY_INV)
thbw = cv2.erode(thbw, np.ones((2, 2), np.uint8), iterations=2)

cntrs, hier = cv2.findContours(thbw.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cntrs = sorted(cntrs, key=cv2.contourArea, reverse=True)

print len(cntrs)
counter = 1

rectangles = []
for c in cntrs:
    r = c_x, c_y, c_w, c_h = cv2.boundingRect(c)
    a = cv2.contourArea(c)
    b = (img.shape[0]-3) * (img.shape[1]-3)

    contour_area_Threshold = 1
    is_inside = False
    for q in rectangles:
        if insideArea(r, q):
            is_inside = True
            break

    flag = False
    if not is_inside:
        #
        if (not a == b) and (a > contour_area_Threshold):
            #
            for q in rectangles:
                if insideXLine(r, q):
                    flag = True
                    x1, y1, w1, h1 = r
                    x2, y2, w2, h2 = q
                    #cv2.rectangle(img, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 1)
                    #cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 0), 1)

            #
            rectangles.append(r)


for r in rectangles:
    x, y, w, h = r
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

    #wd_x, wd_y, wd_w, wd_h = wrap_digit(r)
    #cv2.rectangle(img, (wd_x, wd_y), (wd_x+wd_w, wd_y+wd_h), (0, 255, 0), 1)
    #roi = thbw[wd_y:wd_y+wd_h, wd_x:wd_x+wd_w]

    #title = 'test' + str(counter)
    #cv2.imshow(title, roi)
    #counter += 1



cv2.imshow('test', img)
cv2.imwrite('./testdata/sample/result.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
