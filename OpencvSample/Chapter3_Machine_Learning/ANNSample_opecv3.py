# _*_ coding= utf-8 _*_
import cv2
import numpy as np
from random import randint

animal_net = cv2.ml.ANN_MLP_create()

animal_net.setTrainMethod(cv2.ml.ANN_MLP_RPROP | cv2.ml.ANN_MLP_UPDATE_WEIGHTS)
animal_net.setActivationFunction(cv2.ml.ANN_MLP_SIGMOID_SYM)
animal_net.setLayerSizes(np.array([3, 10, 4]))
animal_net.setTermCriteria((cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 100, 0.1))

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

SAMPLES = 5000
for x in range(0, SAMPLES):
    #print "Samples %d/%d" % (x, SAMPLES)
    animal_net.train(np.array([dog_sample()], dtype=np.float32),
                     cv2.ml.ROW_SAMPLE, np.array([dog_class()], dtype=np.float32))
    animal_net.train(np.array([condor_sample()], dtype=np.float32),
                     cv2.ml.ROW_SAMPLE, np.array([condor_class()], dtype=np.float32))
    animal_net.train(np.array([dolphin_sample()], dtype=np.float32),
                     cv2.ml.ROW_SAMPLE, np.array([dolphin_class()], dtype=np.float32))
    animal_net.train(np.array([dragon_sample()], dtype=np.float32),
                     cv2.ml.ROW_SAMPLE, np.array([dragon_class()], dtype=np.float32))

print "dog", animal_net.predict(np.array([dog_sample()], dtype=np.float32))
print "condor", animal_net.predict(np.array([condor_sample()], dtype=np.float32))
print "dolphin", animal_net.predict(np.array([dolphin_sample()], dtype=np.float32))
print "dragon", animal_net.predict(np.array([dragon_sample()], dtype=np.float32))
