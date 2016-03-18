# _*_ coding= utf-8 _*_

import numpy as np
import cv2
from matplotlib import pyplot as plt

x = np.random.randint(25, 100, 25)
y = np.random.randint(175, 255, 25)

z = np.hstack((x, y))
z = z.reshape((-1, 1))  # z[: np.newaxis]
z = np.float32(z)

# Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# Set flags (Just to avoid line break in the code)
flags = cv2.KMEANS_RANDOM_CENTERS

# Apply KMeans
compactness, labels, centers = cv2.kmeans(data=z, K=2, bestLabels=None, criteria=criteria, attempts=10, flags=flags)

# Split the data to different clusters depending on their labels
A = z[labels == 0]
B = z[labels == 1]

# Now plot 'A' in red, 'B' in blue, 'centers' in yellow
plt.hist(A, 256, [0, 256], color='r')
plt.hist(B, 256, [0, 256], color='b')
plt.hist(centers, 32, [0, 256], color='y')
plt.show()
