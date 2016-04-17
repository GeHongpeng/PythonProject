# _*_ coding= utf-8 _*_
import cv2
import numpy as np
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

# Load param
# animal_net.load('./data/mlp.xml')

# Set criteria and parameters
criteria = (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, 100, 0.001)
params = dict(term_crit=criteria,
              train_method=cv2.ANN_MLP_TRAIN_PARAMS_BACKPROP,
              bp_dw_scale=0.1,
              bp_moment_scale=0.1)

# Create array for train data and label
train_array = np.zeros((1, 3))
label_array = np.zeros((1, 4), 'float')

# Create train data
records = []
RECORDS = 5000
for x in range(0, RECORDS):

    train_array = np.vstack((train_array, dog_sample()))
    label_array = np.vstack((label_array, dog_class()))

    train_array = np.vstack((train_array, condor_sample()))
    label_array = np.vstack((label_array, condor_class()))

    train_array = np.vstack((train_array, dolphin_sample()))
    label_array = np.vstack((label_array, dolphin_class()))

    train_array = np.vstack((train_array, dragon_sample()))
    label_array = np.vstack((label_array, dragon_class()))

# Set train data for training
train_data = train_array[1:, :]
train_resp = label_array[1:, :]

# Start training
animal_net.train(train_data, train_resp, None, params=params)

# Save param
# animal_net.save('./data/mlp.xml')

# Get accuray
dog_results = 0
condor_results = 0
dolphin_results = 0
dragon_results = 0
for x in range(0, 100):
    dog_ret, dog_resp = animal_net.predict(np.array([dog_sample()], dtype=np.float32))
    dog_prediction = dog_resp.argmax(-1)
    if dog_prediction == 0:
        dog_results += 1

    condor_ret, condor_resp = animal_net.predict(np.array([condor_sample()], dtype=np.float32))
    condor_prediction = condor_resp.argmax(-1)
    if condor_prediction == 1:
        condor_results += 1

    dolphin_ret, dolphin_resp = animal_net.predict(np.array([dolphin_sample()], dtype=np.float32))
    dolphin_prediction = dolphin_resp.argmax(-1)
    if dolphin_prediction == 2:
        dolphin_results += 1

    dragon_ret, dragon_resp = animal_net.predict(np.array([dragon_sample()], dtype=np.float32))
    dragon_prediction = dragon_resp.argmax(-1)
    if dragon_prediction == 3:
        dragon_results += 1

print "Dog accuracy: %f" % dog_results
print "Condor accuracy: %f" % condor_results
print "Dolphin accuracy: %f" % dolphin_results
print "Dragon accuracy: %f" % dragon_results
