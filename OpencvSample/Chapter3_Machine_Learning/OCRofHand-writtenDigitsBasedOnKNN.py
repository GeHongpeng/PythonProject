# _*_ coding= utf-8 _*_

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./data/digits.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Now we split the image to 5000 cells, each 20x20 size
# cells is a list
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]

# Make it into a Numpy array. It size will be (50,100,20,20)
x = np.array(cells)

# Now we prepare train_data and test_data.
trainData = x[:, :50].reshape(-1, 400).astype(np.float32)  # Size = (2500,400)
testData = x[:, 50:100].reshape(-1, 400).astype(np.float32)  # Size = (2500,400)

# Create labels for train and test data
k = np.arange(10)
train_labels = np.repeat(k, 250)[:, np.newaxis]
test_labels = train_labels.copy()

#
fail_array = testData
cal_num = 1
while not len(fail_array) == 0:
    # Initiate kNN, train the data, then test it with test data for k=1
    knn = cv2.KNearest()
    knn.train(trainData, train_labels)
    ret, result, neighbours, dist = knn.find_nearest(testData, k=5)

    # Find failed pattern
    tmp_array = result == test_labels
    fail_array = testData[tmp_array.ravel() == False]
    fail_labels = test_labels[tmp_array.ravel() == False]

    # Add to trainData
    trainData = np.vstack((trainData, fail_array))
    train_labels = np.vstack((train_labels, fail_labels))

    # Now we check the accuracy of classification
    # For that, compare the result with test_labels and check which are wrong
    correct = np.count_nonzero(result == test_labels)
    accuracy = correct * 100.0 / result.size
    print '#%d  failed data num:%d  accuracy:%.2f%%' % (cal_num, len(fail_array), accuracy)

    cal_num += 1

"""
# It would be better to convert the data to np.uint8 first and then save it.
# Then while loading, you can convert back into float32
np.savez('./data/digits_knn_data.npz', trainData=trainData.astype(np.uint8), train_labels=train_labels)

# Now load the data
with np.load('./data/digits_knn_data.npz') as data:
    print data.files
    train = data['trainData'].astype(np.float32)
    train_labels = data['train_labels']
"""
