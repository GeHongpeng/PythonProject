# _*_ coding: utf-8 _*_

import numpy as np
import cv2

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3,
                                     minNeighbors=5, minSize=(30,30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)

    if len(rects) == 0:
        return []

    rects[:,2:] += rects[:,:2]
    print rects
    return rects

def draw_rects(img, rects, color):
    for x1,y1,x2,y2 in rects:
        cv2.rectangle(img, (x1,y1), (x2,y2), color, 2)

cap = cv2.VideoCapture(0)

cascade_fn = '/usr/local/Cellar/opencv/2.4.12_2/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_fn)

while True:
    ret, img = cap.read()

    rects = detect(img, cascade)
    draw_rects(img, rects, (0, 255, 0))

    cv2.imshow('Video', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
