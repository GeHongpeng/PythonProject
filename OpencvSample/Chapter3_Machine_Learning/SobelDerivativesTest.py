# _*_ coding= utf-8 _*_
import cv2
import numpy as np

img = cv2.imread("./data/plus.jpg", 0)

x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)

absX = cv2.convertScaleAbs(x)   # 转回uint8
absY = cv2.convertScaleAbs(y)

dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

# 对原图像使用 GaussianBlur 降噪 ( 内核大小 = 3 )
tmp = cv2.GaussianBlur(img, (3, 3), 0)

tmp_x = cv2.Sobel(tmp, cv2.CV_16S, 1, 0)
tmp_y = cv2.Sobel(tmp, cv2.CV_16S, 0, 1)

tmp_absX = cv2.convertScaleAbs(tmp_x)   # 转回uint8
tmp_absY = cv2.convertScaleAbs(tmp_y)

tmp_dst = cv2.addWeighted(tmp_absX, 0.5, tmp_absY, 0.5, 0)


cv2.imshow("img", img)
cv2.imshow("absX", absX)
cv2.imshow("absY", absY)
cv2.imshow("Result", dst)

cv2.imshow("tmp", tmp)
cv2.imshow("tmp_absX", tmp_absX)
cv2.imshow("tmp_absY", tmp_absY)
cv2.imshow("tmp_Result", tmp_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
