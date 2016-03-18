# _*_ coding= utf-8 _*_

import cv2
import numpy as np

"""
使用方向梯度直方图Histogram of Oriented Gradients （HOG）作为特征向量
在计算HOG 前我们使用图片的二阶矩对其进行抗扭斜（deskew）处理
"""

SZ = 20
bin_n = 16 # Number of bins

svm_params = dict(kernel_type=cv2.SVM_LINEAR,
                  svm_type=cv2.SVM_C_SVC,
                  C=2.67, gamma=5.383 )

affine_flags = cv2.WARP_INVERSE_MAP|cv2.INTER_LINEAR

# Define a function which takes a digit image and deskew it
def deskew(img):
    m = cv2.moments(img)
    if abs(m['mu02']) < 1e-2:
        return img.copy()

    skew = m['mu11']/m['mu02']
    M = np.float32([[1, skew, -0.5 * SZ * skew], [0, 1, 0]])
    img = cv2.warpAffine(img, M, (SZ, SZ), flags=affine_flags)

    return img

# Define a the HOG Descriptor of each cell
def hog(img):
    # Find Sobel derivatives of each cell in X and Y direction.
    # void Sobel(InputArray src, OutputArray dst, int ddepth, int xorder, int yorder, int ksize=3, double scale=1, double delta=0, int borderType=BORDER_DEFAULT )
    # gx: InputArray=img, ddepth=cv2.CV_32F, xorder=1, yorder=0
    # gy: InputArray=img, ddepth=cv2.CV_32F, xorder=0, yorder=1
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)  # 求X方向导数
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)  # 求Y方向导数

    # Calculates the magnitude and direction of gradient at each pixel of 2D vectors.
    mag, ang = cv2.cartToPolar(gx, gy)

    # This gradient is quantized to 16 integer values.(0...16)
    bins = np.int32(bin_n * ang /(2 * np.pi))

    # Divide this image to four sub-squares.
    bin_cells = bins[:10, :10], bins[10:, :10], bins[:10, 10:], bins[10:, 10:]
    mag_cells = mag[:10, :10], mag[10:, :10], mag[:10, 10:], mag[10:, 10:]

    # For each sub-square, calculate the histogram of direction (16 bins) weighted with their magnitude.
    # bincount example:
    # b = array([2, 3, 3, 0, 1, 4, 2, 4])
    # np.bincount(b) >>> array([1, 1, 2, 2, 2]) 分别是0 1 2 3 4在数组b中出现的个数
    # w = array([ 0.29529445, 0.4554129 , 0.69615963, 0.4766137 , 0.97929591,0.46069939, 0.76476676, 0.74556715])
    # np.bincount(b,w) >>> array([ 0.4766137 , 0.97929591, 1.06006121, 1.15157254, 1.20626654]) 分别是 0 1 2 3 4的权重和
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]

    # hist is a 64 bit vector
    hist = np.hstack(hists)

    return hist

img = cv2.imread('./data/digits.png', 0)

cells = [np.hsplit(row, 100) for row in np.vsplit(img, 50)]

# First half is trainData, remaining is testData
train_cells = [i[:50] for i in cells]
test_cells = [i[50:] for i in cells]

######     Create training data     ########################
# map: 对可迭代函数'iterable'中的每一个元素应用‘function’方法，将结果作为list返回
deskewed = [map(deskew, row) for row in train_cells]
hogdata = [map(hog, row) for row in deskewed]

trainData = np.float32(hogdata).reshape(-1, bin_n*4)
responses = np.float32(np.repeat(np.arange(10), 250)[:, np.newaxis])

######     Create testing data     ########################
deskewed = [map(deskew, row) for row in test_cells]
hogdata = [map(hog, row) for row in deskewed]
testData = np.float32(hogdata).reshape(-1, bin_n*4)
test_labels = responses.copy()

fail_array = testData
cal_num = 1
while not len(fail_array) == 0:
    ######     Now training     ########################
    svm = cv2.SVM()
    svm.train(trainData,responses, params=svm_params)
    #svm.save('./data/svm_data.dat')

    ######     Now training     ########################
    result = svm.predict_all(testData)

    # Find failed pattern
    tmp_array = result == test_labels
    fail_array = testData[tmp_array.ravel() == False]
    fail_labels = test_labels[tmp_array.ravel() == False]

    # Add to trainData
    trainData = np.vstack((trainData, fail_array))
    responses = np.vstack((responses, fail_labels))

    #######   Check Accuracy   ########################
    mask = result==test_labels
    correct = np.count_nonzero(mask)
    accuracy = correct * 100.0 / result.size

    print '#%d failed data num:%d  accuracy:%.2f%%' % (cal_num, len(fail_array), accuracy)
    cal_num += 1
