# -*- coding: UTF-8 -*-

import cv2
from sklearn import svm
from sklearn.metrics import accuracy_score
from mnist import mnist_loader

# load
training_data, validation_data, test_data = mnist_loader.load_data()

# train
print 'Start training'
e0 = cv2.getTickCount()

clf = svm.SVC()
clf.fit(training_data[0][:1000], training_data[1][:1000])

print 'End training'
e00 = cv2.getTickCount()
time0 = (e00 - e0) / cv2.getTickFrequency()
print 'Training data duration: %.3fs' % time0

# test
predictions = [int(a) for a in clf.predict(test_data[0])]
num_correct = sum(int(a == y) for a, y in zip(predictions, test_data[1]))
print "Baseline classifier using an SVM."
print "%s of %s values correct." % (num_correct, len(test_data[1]))

print 'Accuracy Score: {0}%'.format(accuracy_score(test_data[1], predictions) * 100)
