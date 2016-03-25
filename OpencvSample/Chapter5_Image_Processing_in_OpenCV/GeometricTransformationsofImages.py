# _*_ coding= utf-8 _*_
import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
Scaling
"""
img = cv2.imread('./data/lion.jpg')

res1 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

#OR

height, width = img.shape[:2]
res2 = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)

cv2.imshow('image1', res1)
cv2.imshow('image2', res2)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Translation

Third argument of the cv2.warpAffine() function is the size of the output image,
which should be in the form of (width, height).
Remember width = number of columns, and height = number of rows.
"""
img = cv2.imread('./data/lion.jpg', 0)
rows, cols = img.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Rotation
"""
img = cv2.imread('./data/lion.jpg', 0)
rows, cols = img.shape

M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('image', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Affine Transformation
"""
img = cv2.imread('./data/lion.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv2.getAffineTransform(pts1, pts2)

dst = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()

"""
Perspective Transformation
"""
img = cv2.imread('./data/lion.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[56, 65], [368, 52],[28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (300, 300))

cv2.imwrite('./data/lion_PerTrans.jpg', dst)

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
