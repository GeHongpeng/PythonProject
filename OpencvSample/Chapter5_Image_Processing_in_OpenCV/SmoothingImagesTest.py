# _*_ coding= utf-8 _*_

import cv2
import numpy as np

def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1]);
        j = int(np.random.random() * img.shape[0]);
        if img.ndim == 2:
            img[j, i] = 255
        elif img.ndim == 3:
            img[j, i, 0]= 255
            img[j, i, 1]= 255
            img[j, i, 2]= 255
    return img

img = cv2.imread("./data/sample.png", 0)
#result = salt(img, 500)
result = img

tmp_Blur = cv2.blur(result, (3, 3))
tmp_GaussianBlur = cv2.GaussianBlur(result, (3, 3), 0)
tmp_median = cv2.medianBlur(result, 3)

#9---滤波领域直径
#后面两个数字：空间高斯函数标准差，灰度值相似性标准差
tmp_bilateralBlur = cv2.bilateralFilter(result, 9, 21, 21)

cv2.imshow("Origin", img)
cv2.imshow("Blur", tmp_Blur)
cv2.imshow("GaussianBlur", tmp_GaussianBlur)
cv2.imshow("MedianBlur", tmp_median)
cv2.imshow("bilateralBlur", tmp_bilateralBlur)

cv2.waitKey(0)
cv2.destroyAllWindows()
