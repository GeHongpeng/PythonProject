# _*_ coding: utf-8 _*_

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./data/logo.png', 1)

# Accessing and Modifying pixel values
print img.item(10, 10, 2)
img.itemset((10, 10, 2), 100)
print img.item(10, 10, 2)

# Shape of image
print img.shape

# Total number of pixels
print img.size

# Image datatype
print img.dtype

# Splitting Image Channels
# cv2.split() is a costly operation (in terms of time), so only use it if necessary.
# Numpy indexing is much more efficient and should be used if possible.
b, g, r = cv2.split(img)  # b = img[:,:,0]

# Merging Image Channels
img_2 = cv2.merge((b, g, r))
# cv2.imshow('image', img_2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# RGB color in matplotlib
RED = [255, 0, 0]

replicate = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=RED)

plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()
