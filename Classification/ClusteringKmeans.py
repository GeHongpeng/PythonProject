# _*_ coding= utf-8 _*_

import cv2
import numpy as np
import os
import glob
import csv

# Number of bins
bin_n = 16

# Define a the HOG Descriptor of each cell
def hog(img):
    # Find Scharr derivatives of each cell in X and Y direction.
    gx = cv2.Scharr(img, cv2.CV_32F, 1, 0)
    gy = cv2.Scharr(img, cv2.CV_32F, 0, 1)

    # Calculates the magnitude and direction of gradient at each pixel of 2D vectors.
    mag, ang = cv2.cartToPolar(gx, gy)

    # This gradient is quantized to 16 integer values.(0...16)
    bins = np.int32(bin_n * ang / (2 * np.pi))

    # Divide this image to four sub-squares.
    bin_cells = bins[:10, :10], bins[10:, :10], bins[:10, 10:], bins[10:, 10:]
    mag_cells = mag[:10, :10], mag[10:, :10], mag[:10, 10:], mag[10:, 10:]

    #
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]

    # hist is a 64 bit vector
    hist = np.hstack(hists)

    return hist

"""
Clustering-KMeans
"""
# 特徴量を算出
dataArray = np.array([]).reshape(0, 64)
imageFiles = glob.glob('./data/*.jpg')
for imageFile in imageFiles:
    img = cv2.imread(imageFile, 0)
    result = hog(img)
    dataArray = np.vstack((dataArray, result))
# convert to np.float32
dataArray = np.float32(dataArray)

# define criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# Set flags (Just to avoid line break in the code)
flags = cv2.KMEANS_RANDOM_CENTERS
# Apply KMeans
ret, label, center = cv2.kmeans(data=dataArray, K=10, bestLabels=None, criteria=criteria, attempts=50, flags=flags)
# print result
print label
