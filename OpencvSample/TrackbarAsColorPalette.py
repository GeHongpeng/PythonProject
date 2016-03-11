# _*_ coding: utf-8 _*_

import cv2
import numpy as np

# Define callback function
def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

# Create Trackbar
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()

"""
# 当鼠标按下时变为True
drawing = False

# 如果mode 为true 绘制矩形。按下'm' 变成绘制曲线。
mode = True
ix,iy = -1,-1

# Define callback function
def draw_circle(event, x, y, flags, param):
    r=cv2.getTrackbarPos('R', 'image')
    g=cv2.getTrackbarPos('G', 'image')
    b=cv2.getTrackbarPos('B', 'image')
    color = (b,g,r)

    global ix,iy,drawing,mode
    # 
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    # 
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), color, -1)
            else:
                # 
                cv2.circle(img, (x, y), 3, color, -1)
                # 
                # r=int(np.sqrt((x-ix)**2+(y-iy)**2))
                # cv2.circle(img,(x,y),r,(0,0,255),-1)
    # 。
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False
        # if mode == True:
            # cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        # else:
            # cv2.circle(img,(x,y),5,(0,0,255),-1)

cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()
"""
