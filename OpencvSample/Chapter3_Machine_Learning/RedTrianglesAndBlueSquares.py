# _*_ coding= utf-8 _*_

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Feature set containing (x,y) values of 25 known/training data
trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)

# Labels each one either Red or Blue with numbers 0 and 1
responses = np.random.randint(0, 2, (25, 1)).astype(np.float32)

# Take Red families and plot them
red = trainData[responses.ravel() == 0]
plt.scatter(x=red[:, 0], y=red[:, 1], s=80, c='r', marker='^')

# Take Blue families and plot them
blue = trainData[responses.ravel() == 1]
plt.scatter(x=blue[:, 0], y=blue[:, 1], s=80, c='b', marker='s')

# Create a newcomer
newcomer = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(x=newcomer[:, 0], y=newcomer[:, 1], s=80, c='g', marker='o')

knn = cv2.KNearest()
knn.train(trainData, responses)
ret, results, neighbours, dist = knn.find_nearest(newcomer, 5)

print "result: ", results, "\n"
print "neighbours: ", neighbours, "\n"
print "distance: ", dist

plt.show()
