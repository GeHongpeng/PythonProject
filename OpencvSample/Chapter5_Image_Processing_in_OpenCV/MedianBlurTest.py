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
result = salt(img, 500)

# 函数返回处理结果，
# 第一个参数是待处理图像，
# 第二个参数是孔径的尺寸，一个大于1的奇数。
# 比如这里是3，中值滤波器就会使用3×3的范围来计算。
# 即对像素的中心值及其3×3邻域组成了一个数值集，对其进行处理计算，当前像素被其中值替换掉。
# 如果在某个像素周围有白色或黑色的像素，这些白色或黑色的像素不会选择作为中值（最大或最小值不用），而是被替换为邻域值
median = cv2.medianBlur(result, 3)
"""
由于中值滤波不会处理最大和最小值，所以就不会受到噪声的影响。
相反，如果直接采用blur进行均值滤波，则不会区分这些噪声点，滤波后的图像会受到噪声的影响。
中值滤波器在处理边缘也有优势。但中值滤波器会清除掉某些区域的纹理（如背景中的树）。
"""

cv2.imshow("Salt", result)
cv2.imshow("Median", median)

cv2.waitKey(0)
