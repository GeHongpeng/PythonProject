# _*_ coding= utf-8 _*_
import cv2
import numpy as np
import glob
from random import randint

# Output of the Neural network
DIGIT = np.array(
    [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]], dtype=np.float32
)

print 'Loading training data...'
e0 = cv2.getTickCount()

#
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
train_labels = np.zeros((1, 10), 'float')
for i in range(0, 10):
    for j in range(0, 250):
        train_labels = np.vstack((train_labels, DIGIT[i]))
train_labels = train_labels[1:, :]
test_labels = train_labels.copy()

#
e00 = cv2.getTickCount()
time0 = (e00 - e0) / cv2.getTickFrequency()
print 'Loading data duration: %.3fs' % time0

# set start time
e1 = cv2.getTickCount()

# Create MLP
layer_sizes = np.int32([400, 57, 10])
digit_net = cv2.ANN_MLP()
digit_net.create(layer_sizes)

print 'Neural network layer: ', layer_sizes

# Load parameter
# animal_net.load('./data/mlp.xml')

# Set criteria and parameters
criteria = (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, 1000, 0.0001)
params = dict(term_crit=criteria,
              train_method=cv2.ANN_MLP_TRAIN_PARAMS_BACKPROP,
              bp_dw_scale=0.001,
              bp_moment_scale=0.1)

print 'Training MLP ...'

# Start training
digit_net.train(trainData, train_labels, None, params=params)

# set end time
e2 = cv2.getTickCount()
time = (e2 - e1) / cv2.getTickFrequency()
print 'Training duration: %.3fs' % time

# Save param
# animal_net.save('./data/mlp.xml')

# Start testing
print 'Testing...'
ret, resp = digit_net.predict(testData)
prediction = resp.argmax(-1)
#print 'Prediction:', prediction

true_resp = test_labels.argmax(-1)
#print 'True response:', true_resp

# Calculate accuray
num_correct = np.sum(true_resp == prediction)
print 'Correct number: %d' % num_correct

test_rate = np.mean(prediction == true_resp)
print 'Test rate: %.2f%%' % (test_rate * 100)
