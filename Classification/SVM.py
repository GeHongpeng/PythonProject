# _*_ coding= utf-8 _*_

import cv2
import numpy as np

# Load the data, converters convert the letter to a number
data = np.loadtxt('./hog/hog.csv', dtype='float32', delimiter=',')

# split the data to two, 10000 each for train and test
train, test = np.vsplit(data, 2)

# split trainData and testData to features and responses
responses, trainData = np.hsplit(train, [1])
test_labels, testData = np.hsplit(test, [1])

# convert the type of responses and test_labels to int
responses = np.int32(responses)
test_labels = np.int32(test_labels)

# initialize
fail_array = testData
cal_num = 1
svm_params = dict(kernel_type=cv2.SVM_LINEAR, svm_type=cv2.SVM_C_SVC, C=2.67, gamma=5.383)
affine_flags = cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR

# Training
svm = cv2.SVM()
svm.train(trainData, responses, params=svm_params)
#svm.save('./data/svm_data.dat')

# predicting
result = np.int32(svm.predict_all(testData))
print result

"""
while not len(fail_array) == 0:
    # Training
    svm = cv2.SVM()
    svm.train(trainData, responses, params=svm_params)
    #svm.save('./data/svm_data.dat')

    # predicting
    result = svm.predict_all(testData)
    print result

    # Find failed pattern
    tmp_array = result == test_labels
    fail_array = testData[tmp_array.ravel()==False]
    fail_labels = test_labels[tmp_array.ravel()==False]

    # Add to trainData
    trainData = np.vstack((trainData, fail_array))
    responses = np.vstack((responses, fail_labels))

    # Check Accuracy
    mask = result==test_labels
    correct = np.count_nonzero(mask)
    accuracy = correct * 100.0 / result.size

    print '#%d failed data num:%d  accuracy:%.2f%%' % (cal_num, len(fail_array), accuracy)
    cal_num += 1
"""
