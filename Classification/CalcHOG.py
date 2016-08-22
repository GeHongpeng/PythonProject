# _*_ coding= utf-8 _*_

import cv2
import numpy as np
import os
import glob
import csv

# Number of bins
bin_n = 16

# Define a the HOG Descriptor of each cell
def hog(img):
    # Find Scharr derivatives of each cell in X and Y direction.
    gx = cv2.Scharr(img, cv2.CV_32F, 1, 0)
    gy = cv2.Scharr(img, cv2.CV_32F, 0, 1)

    # Calculates the magnitude and direction of gradient at each pixel of 2D vectors.
    mag, ang = cv2.cartToPolar(gx, gy)

    # This gradient is quantized to 16 integer values.(0...16)
    bins = np.int32(bin_n * ang / (2 * np.pi))

    # Divide this image to four sub-squares.
    bin_cells = bins[:827, :1170], bins[827:, :1170], bins[:827, 1170:], bins[827:, 1170:]
    mag_cells = mag[:827, :1170], mag[827:, :1170], mag[:827, 1170:], mag[827:, 1170:]

    #
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]

    # hist is a 64 bit vector
    hist = np.hstack(hists)

    return hist

# 特徴量を算出し、csvファイルへ保存
fw = open('./hog/hog.csv', 'ab')
csvWriter = csv.writer(fw)

# 特徴量を算出し、csvファイルへ保存
dataArray = np.float32(np.array([]).reshape(0, 65))
imageFiles = glob.glob('./data2/*.jpg')
for imageFile in imageFiles:
    # ファイル名（種別）を取得
    fileNameWithoutExtension = os.path.splitext(os.path.basename(imageFile))[0]
    # 画像ファイルを読み込む
    img = cv2.imread(imageFile, 0)
    # HOG特徴量を算出
    result = np.float32(hog(img)).astype(str)
    # 各特徴量の先頭に種別情報を追加
    result = np.insert(result, 0, fileNameWithoutExtension)
    # 生成したデータを配列に格納
    dataArray = np.vstack((dataArray, result))
    # ファイルへ出力
    csvWriter.writerow(result)
