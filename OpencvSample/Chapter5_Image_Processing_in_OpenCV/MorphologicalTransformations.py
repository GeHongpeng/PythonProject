# _*_ coding= utf-8 _*_
import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
1. Erosion

erode(src, dst, element=None, iterations=1) → None
Parameters:
src – input image; the number of channels can be arbitrary,
      but the depth should be one of CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
dst – output image of the same size and type as src.
element – structuring element used for erosion;
          if element=Mat() , a 3 x 3 rectangular structuring element is used.
iterations – number of times erosion is applied.
"""
img = cv2.imread('./data/j.png', 0)
kernel = np.ones((5, 5), np.uint8)

# Erosion
erosion = cv2.erode(img, kernel, iterations=1)


plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(erosion), plt.title('Erosion')
plt.xticks([]), plt.yticks([])
plt.show()


"""
2. Dilation

dilate(src, dst, element=None, iterations=1) → None
Parameters:
src – input image; the number of channels can be arbitrary,
      but the depth should be one of CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
dst – output image of the same size and type as src.
element – structuring element used for dilation;
          if element=Mat() , a 3 x 3 rectangular structuring element is used.
iterations – number of times dilation is applied.
"""
img = cv2.imread('./data/j.png', 0)
kernel = np.ones((5, 5), np.uint8)

# Dilation
dilation = cv2.dilate(img, kernel, iterations=1)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dilation), plt.title('Dilation')
plt.xticks([]), plt.yticks([])
plt.show()


"""
3. Opening

erode(src, dst, element=None, iterations=1) → None
Parameters:
src – input image; the number of channels can be arbitrary,
      but the depth should be one of CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
dst – output image of the same size and type as src.
element – structuring element used for erosion;
          if element=Mat() , a 3 x 3 rectangular structuring element is used.
iterations – number of times erosion is applied.
"""
def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        if img.ndim == 2:
            img[j, i] = 255
        elif img.ndim == 3:
            img[j, i, 0] = 255
            img[j, i, 1] = 255
            img[j, i, 2] = 255
    return img

img = cv2.imread('./data/j.png', 0)
kernel = np.ones((5, 5), np.uint8)

img_salt = salt(img, 500)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

plt.subplot(121), plt.imshow(img_salt), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(opening), plt.title('Opening')
plt.xticks([]), plt.yticks([])
plt.show()


"""
4. Closing

morphologyEx(src, dst, temp, element, operation, iterations=1) → None
Parameters:
src – input image; the number of channels can be arbitrary,
      but the depth should be one of CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
dst – output image of the same size and type as src.
element – structuring element used for erosion;
          if element=Mat() , a 3 x 3 rectangular structuring element is used.
iterations – number of times erosion is applied.

"""
img = cv2.imread('./data/closing_j.png', 0)
kernel = np.ones((5, 5), np.uint8)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(closing), plt.title('Closing')
plt.xticks([]), plt.yticks([])
plt.show()


"""
5. Morphological Gradient

morphologyEx(src, dst, temp, element, operation, iterations=1) → None
Parameters:
src – input image; the number of channels can be arbitrary,
      but the depth should be one of CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
dst – output image of the same size and type as src.
element – structuring element used for erosion;
          if element=Mat() , a 3 x 3 rectangular structuring element is used.
iterations – number of times erosion is applied.

"""
img = cv2.imread('./data/j.png', 0)
kernel = np.ones((5, 5), np.uint8)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(gradient), plt.title('Morphological Gradient')
plt.xticks([]), plt.yticks([])
plt.show()


"""
6. Top Hat

morphologyEx(src, dst, temp, element, operation, iterations=1) → None
Parameters:
src – input image; the number of channels can be arbitrary,
      but the depth should be one of CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
dst – output image of the same size and type as src.
element – structuring element used for erosion;
          if element=Mat() , a 3 x 3 rectangular structuring element is used.
iterations – number of times erosion is applied.
"""
img = cv2.imread('./data/j.png', 0)
kernel = np.ones((9, 9), np.uint8)

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(tophat), plt.title('Top Hat')
plt.xticks([]), plt.yticks([])
plt.show()


"""
7. Black Hat

morphologyEx(src, dst, temp, element, operation, iterations=1) → None
Parameters:
src – input image; the number of channels can be arbitrary,
      but the depth should be one of CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
dst – output image of the same size and type as src.
element – structuring element used for erosion;
          if element=Mat() , a 3 x 3 rectangular structuring element is used.
iterations – number of times erosion is applied.
"""
img = cv2.imread('./data/j.png', 0)
kernel = np.ones((9, 9), np.uint8)

blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blackhat), plt.title('Black Hat')
plt.xticks([]), plt.yticks([])
plt.show()


"""
Structuring Element

getStructuringElement(shape, ksize[, anchor]) → retval
Parameters:
shape – Element shape that could be one of the following:
        MORPH_RECT
        MORPH_ELLIPSE
        MORPH_CROSS
        CV_SHAPE_CUSTOM
ksize – Size of the structuring element.
anchor – Anchor position within the element.
         The default value (-1, -1) means that the anchor is at the center.
         Note that only the shape of a cross-shaped element depends on the anchor position.
         In other cases the anchor just regulates how much the result of the morphological
         operation is shifted.
"""
print cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
print cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
print cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
