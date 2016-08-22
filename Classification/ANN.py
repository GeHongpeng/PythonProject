# _*_ coding= utf-8 _*_
import cv2
import numpy as np


def float_formatter(x):
    return "%.3f" % x


def type_class(documentType):
    if documentType == 1:
        return [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif documentType == 2:
        return [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    elif documentType == 3:
        return [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    elif documentType == 4:
        return [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    elif documentType == 5:
        return [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    elif documentType == 6:
        return [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    elif documentType == 7:
        return [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    elif documentType == 8:
        return [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    elif documentType == 9:
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    elif documentType == 10:
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]


def calc_resp(respArray):
    #
    resultList = []
    resultArray = np.array([]).reshape(0, 11)

    #
    for itemIndex in range(len(respArray)):
        #
        targetArray = respArray[itemIndex]
        index1 = respArray[itemIndex].argmax(-1)
        #
        maxValue1 = targetArray[index1]

        #
        targetArray = np.delete(targetArray, index1, axis=0)

        #
        index2 = targetArray.argmax(-1)
        #
        maxValue2 = targetArray[index2]

        #
        if maxValue1 >= 1 and maxValue2 >= 1:
            resultList.append(np.zeros((1, 11)))
            continue
        #
        """
        if maxValue1 < 0.8:
            resultList.append(np.zeros((1, 11)))
            continue
        """

        #
        resultList.append(type_class(index1))

    #
    RECORDS = len(resultList)
    for x in range(0, RECORDS):
        resultArray = np.vstack((resultArray, resultList[x]))

    return np.int32(resultArray)

# Load the train data
data = np.loadtxt('./2_hog_train/hog_train.csv', dtype='float32', delimiter=',')
# split data to responses and trainData
responses, trainData = np.hsplit(data, [1])
# Create arrays for train data and response
train_array = np.float32(np.array([]).reshape(0, 64))
train_resp_array = np.float32(np.array([]).reshape(0, 11))
# Create train data
TRAIN_RECORDS = len(trainData)
for x in range(0, TRAIN_RECORDS):
    train_array = np.vstack((train_array, trainData[x]))
    train_resp_array = np.vstack((train_resp_array, type_class(responses[x])))
# Set train data for training
train_data = train_array
train_resp = train_resp_array


# Load the test data
data = np.loadtxt('./3_hog_test/hog_test.csv', dtype='float32', delimiter=',')
# split data to test_labels and testData
testLabels, testData = np.hsplit(data, [1])

# Create arrays for test data and label
test_array = np.float32(np.array([]).reshape(0, 64))
test_resp_array = np.float32(np.array([]).reshape(0, 11))
# Create test data
TEST_RECORDS = len(testData)
for x in range(0, TEST_RECORDS):
    test_array = np.vstack((test_array, testData[x]))
    test_resp_array = np.vstack((test_resp_array, type_class(testLabels[x])))
# Set test data for testing
test_data = test_array
test_resp = test_resp_array


# Create MLP
layer_sizes = np.int32([64, 35, 11])
animal_net = cv2.ANN_MLP()
animal_net.create(layer_sizes)
# Set criteria and parameters
criteria = (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, 500, 0.0001)
params = dict(term_crit=criteria,
              train_method=cv2.ANN_MLP_TRAIN_PARAMS_BACKPROP,
              bp_dw_scale=0.001,
              bp_moment_scale=0.1)
# Start training
animal_net.train(train_data, train_resp, None, params=params)


# Predict
ret, resp = animal_net.predict(test_data)
# Calculate responses
resp = calc_resp(resp)
# Formatting
#resp = np.array([map(float_formatter, row) for row in resp])
# Print result
for i in range(len(resp)):
    print "****************************************"
    print "No:", i + 1
    print "true   :", np.int32(test_resp[i])
    print "predict:", resp[i]#.astype(float)
    print "documentType:", resp[i].argmax(-1)
    print "****************************************"

# Print aggregate results
print "\n------------------------------------"
true_resp = test_resp.argmax(-1)
print 'True response:', true_resp

prediction = resp.argmax(-1)
print 'Prediction:', prediction

num_correct = np.sum(true_resp == prediction)
print 'Correct number: %d' % num_correct

test_rate = np.mean(prediction == true_resp)
print 'Test rate: %.2f%%' % (test_rate * 100)
print "------------------------------------"
