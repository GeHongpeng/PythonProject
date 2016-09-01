# _*_ coding= utf-8 _*_

import sys
sys.path.append("/usr/local/Cellar/numpy/1.11.0/lib/python2.7/site-packages")
sys.path.append("/usr/local/Cellar/opencv/2.4.12_2/lib/python2.7/site-packages")


import numpy as np
import cv2
import os
import re
import json

# コマンドライン引数を取得
params = sys.argv

targetImageFile = params[1]
maskFileOutputPath = params[2]

#
img = cv2.imread(targetImageFile, 1)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#
rsz = gray.copy()
ret, bw = cv2.threshold(rsz, 200, 255, cv2.THRESH_BINARY_INV)

# detect horizontal line
horizontal = bw.copy()
scale = 25
height, width = horizontal.shape
horizontalsize = width / scale
horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontalsize, 1))
horizontal = cv2.erode(horizontal, horizontalStructure)
horizontal = cv2.dilate(horizontal, horizontalStructure)

# detect vertical line
vertical = bw.copy()
scale = 25
height, width = vertical.shape
verticalsize = height / scale
verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, verticalsize))
vertical = cv2.erode(vertical, verticalStructure)
vertical = cv2.dilate(vertical, verticalStructure)

#
mask = horizontal + vertical

#
jointPoints = cv2.bitwise_and(horizontal, vertical)

#
contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# contours = sorted(contours, key=cv2.contourArea, reverse=True)

#
contoursList = []
for c in contours:
    # 輪郭エリアを算出する
    a = cv2.contourArea(c)
    if a < 100:
        continue

    #
    contoursPoly = cv2.approxPolyDP(c, 3, True)
    boundRect = cv2.boundingRect(contoursPoly)

    x1, y1, w, h = cv2.boundingRect(contoursPoly)
    #
    if (w <= 5) or (h <= 60):
        continue

    #
    sub_contours, sub_hierarchy = cv2.findContours(mask[y1:y1 + h, x1:x1 + w], cv2.RETR_CCOMP,
                                                   cv2.CHAIN_APPROX_SIMPLE)
    if len(sub_contours) <= 1:
        continue

    #
    contoursList.append((x1, y1, w, h))

#
contoursList = sorted(contoursList, key=lambda x: (x[0], x[1]), reverse=False)

#
fileName = os.path.basename(targetImageFile)
resultFile = os.path.splitext(fileName)[0]

#
tableList = []
for contour in contoursList:
    #
    x1, y1, w, h = contour
    #result = str(x1) + ' ' + str(y1) + ' ' + str(x1 + w) + ' ' + str(y1 + h) + "\n"

    #
    leftTop = {"X": x1, "Y": y1}
    rightBottom = {"X": x1+w, "Y": y1+h}
    table = {"LT": leftTop, "RB": rightBottom}

    #
    tableList.append(table)

jsonstring = json.dumps(tableList, indent=4)
print(jsonstring)

cv2.imwrite(resultFile + "_mask.jpg", mask)

"""
targetFilePath = './input/'
resultFilePath = './output/'

fileList = os.listdir(targetFilePath)
for fileName in fileList:
    #
    jpg = re.compile("jpg")
    if jpg.search(fileName):
        #
        img = cv2.imread(targetFilePath + fileName, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        #
        rsz = gray.copy()
        ret, bw = cv2.threshold(rsz, 200, 255, cv2.THRESH_BINARY_INV)

        # detect horizontal line
        horizontal = bw.copy()
        scale = 25
        height, width = horizontal.shape
        horizontalsize = width / scale
        horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontalsize, 1))
        horizontal = cv2.erode(horizontal, horizontalStructure)
        horizontal = cv2.dilate(horizontal, horizontalStructure)

        # detect vertical line
        vertical = bw.copy()
        scale = 25
        height, width = vertical.shape
        verticalsize = height / scale
        verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, verticalsize))
        vertical = cv2.erode(vertical, verticalStructure)
        vertical = cv2.dilate(vertical, verticalStructure)

        #
        mask = horizontal + vertical

        #
        jointPoints = cv2.bitwise_and(horizontal, vertical)

        #
        contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #
        # contours = sorted(contours, key=cv2.contourArea, reverse=True)

        #
        contoursList = []
        for c in contours:
            # 輪郭エリアを算出する
            a = cv2.contourArea(c)
            if a < 100:
                continue

            #
            contoursPoly = cv2.approxPolyDP(c, 3, True)
            boundRect = cv2.boundingRect(contoursPoly)

            x1, y1, w, h = cv2.boundingRect(contoursPoly)
            #
            if (w <= 5) or (h <= 60):
                continue

            #
            sub_contours, sub_hierarchy = cv2.findContours(mask[y1:y1 + h, x1:x1 + w], cv2.RETR_CCOMP,
                                                           cv2.CHAIN_APPROX_SIMPLE)
            if len(sub_contours) <= 1:
                continue

            #
            contoursList.append((x1, y1, w, h))

        #
        contoursList = sorted(contoursList, key=lambda x: (x[0], x[1]), reverse=False)

        #
        resultFile = os.path.splitext(fileName)[0]
        f = open(resultFilePath + resultFile + '.txt', 'w')
        for contour in contoursList:
            x1, y1, w, h = contour
            result = str(x1) + ' ' + str(y1) + ' ' + str(x1 + w) + ' ' + str(y1 + h) + "\n"
            cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 1)
            f.write(result)
        f.close()
        # print resultFile

        #cv2.imwrite('./data/result.jpg', img)
    else:
        pass
"""

"""

leftTop = {
    "X": 100,
    "Y": 100
}
rightBottom = {
    "X": 200,
    "Y": 100
}

table = {
    "LT": leftTop,
    "RB": rightBottom
}

tableList = []

tableList.append(table)
tableList.append(table)


jsonstring = json.dumps(tableList, indent=4)
#print(jsonstring)

#decode_json_data = json.loads(jsonstring)
#print decode_json_data)


#cv2.imshow('result', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
"""