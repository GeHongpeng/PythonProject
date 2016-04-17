# _*_ coding= utf-8 _*_
import cv2
import numpy as np
import glob
from random import randint

"""
Input arrays
weight, length, teeth

Output arrays
dog, eagle, dolphin and dragon
"""
def dog_sample():
    return [randint(5, 20), 1, randint(38, 42)]


def dog_class():
    return [1, 0, 0, 0]


def condor_sample():
    return [randint(3, 13), 3, 0]


def condor_class():
    return [0, 1, 0, 0]


def dolphin_sample():
    return [randint(30, 190), randint(5, 15), randint(80, 100)]


def dolphin_class():
    return [0, 0, 1, 0]


def dragon_sample():
    return [randint(1200, 1800), randint(15, 40), randint(110, 180)]


def dragon_class():
    return [0, 0, 0, 1]


def record(sample, classification):
    return (np.array([sample], dtype=np.float32), np.array([classification], dtype=np.float32))

# Create MLP
layer_sizes = np.int32([3, 10, 4])
animal_net = cv2.ANN_MLP()
animal_net.create(layer_sizes)

# Load parameter
# animal_net.load('./data/mlp.xml')

# Set criteria and parameters
criteria = (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, 500, 0.0001)
params = dict(term_crit=criteria,
              train_method=cv2.ANN_MLP_TRAIN_PARAMS_BACKPROP,
              bp_dw_scale=0.001,
              bp_moment_scale=0.1)

# Create arrays for train data and response
train_array = np.zeros((1, 3))
train_resp_array = np.zeros((1, 4), 'float')

# Load train data from files
training_data = glob.glob('./data/train_*.npz')
for single_npz in training_data:
    with np.load(single_npz) as data:
        print data.files
        train_temp = data['train_data']
        train_resp_temp = data['train_resp']

    #
    train_array = np.vstack((train_array, train_temp))
    train_resp_array = np.vstack((train_resp_array, train_resp_temp))

"""
# Create train data
TRAIN_RECORDS = 250
for x in range(0, TRAIN_RECORDS):

    train_array = np.vstack((train_array, dog_sample()))
    train_resp_array = np.vstack((train_resp_array, dog_class()))

    train_array = np.vstack((train_array, condor_sample()))
    train_resp_array = np.vstack((train_resp_array, condor_class()))

    train_array = np.vstack((train_array, dolphin_sample()))
    train_resp_array = np.vstack((train_resp_array, dolphin_class()))

    train_array = np.vstack((train_array, dragon_sample()))
    train_resp_array = np.vstack((train_resp_array, dragon_class()))
"""

# Set train data for training
train_data = train_array[1:, :]
train_resp = train_resp_array[1:, :]

# save training data as a numpy file
# np.savez('./data/train_data.npz', train_data=train_data, train_resp=train_resp)

# Start training
animal_net.train(train_data, train_resp, None, params=params)

# Save param
# animal_net.save('./data/mlp.xml')

# Create arrays for test data and label
test_array = np.zeros((1, 3))
test_resp_array = np.zeros((1, 4), 'float')

# Load test data from files
testing_data = glob.glob('./data/test_*.npz')
for single_npz in testing_data:
    with np.load(single_npz) as data:
        print data.files
        test_temp = data['test_data']
        test_resp_temp = data['test_resp']

    #
    test_array = np.vstack((test_array, test_temp))
    test_resp_array = np.vstack((test_resp_array, test_resp_temp))

"""
# Create test data
TEST_RECORDS = 250
for x in range(0, TEST_RECORDS):

    test_array = np.vstack((test_array, dog_sample()))
    test_resp_array = np.vstack((test_resp_array, dog_class()))

    test_array = np.vstack((test_array, condor_sample()))
    test_resp_array = np.vstack((test_resp_array, condor_class()))

    test_array = np.vstack((test_array, dolphin_sample()))
    test_resp_array = np.vstack((test_resp_array, dolphin_class()))

    test_array = np.vstack((test_array, dragon_sample()))
    test_resp_array = np.vstack((test_resp_array, dragon_class()))
"""

test_data = test_array[1:, :]
test_resp = test_resp_array[1:, :]

# save training data as a numpy file
# np.savez('./data/test_data.npz', test_data=test_data, test_resp=test_resp)

# Calculate accuray
ret, resp = animal_net.predict(test_data)
prediction = resp.argmax(-1)
#print 'Prediction:', prediction

true_resp = test_resp.argmax(-1)
#print 'True response:', true_resp

num_correct = np.sum(true_resp == prediction)
print 'Correct number: %d' % num_correct

test_rate = np.mean(prediction == true_resp)
print 'Test rate: %f' % (test_rate * 100)
