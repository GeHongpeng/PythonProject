# _*_ coding= utf-8 _*_

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the data, converters convert the letter to a number
data= np.loadtxt('./data/letter-recognition.data', dtype='float32', delimiter=',',
                 converters={0: lambda ch: ord(ch)-ord('A')})

# split the data to two, 10000 each for train and test
train, test = np.vsplit(data, 2)

# split trainData and testData to features and responses
responses, trainData = np.hsplit(train, [1])
labels, testData = np.hsplit(test, [1])

#
fail_array = testData
cal_num = 1
while not len(fail_array) == 0:
    # Initiate the kNN, classify, measure accuracy.
    knn = cv2.KNearest()
    knn.train(trainData, responses)
    ret, result, neighbours, dist = knn.find_nearest(testData, k=5)

    # Calculate failed pattern
    tmp_array = result == labels
    fail_array = testData[tmp_array.ravel() == False]
    fail_labels = labels[tmp_array.ravel() == False]

    correct = np.count_nonzero(result == labels)
    accuracy = correct * 100.0 / 10000
    print '#%d  fail data num:%d  accuracy:%.2f%%' % (cal_num, len(fail_array), accuracy)

    #
    trainData = np.vstack((trainData, fail_array))
    responses = np.vstack((responses, fail_labels))
    cal_num += 1

"""
# Save trainData and responses
np.savez('./data/letters_knn_data.npz', trainData=trainData, responses=responses)

# Now load the data
with np.load('./data/letters_knn_data.npz') as knn_data:
    print knn_data.files
    train = knn_data['trainData']
    train_labels = knn_data['responses']
"""
