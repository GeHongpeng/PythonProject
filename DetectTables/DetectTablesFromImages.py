# _*_ coding= utf-8 _*_

import sys
sys.path.append("/usr/local/Cellar/numpy/1.11.0/lib/python2.7/site-packages")
sys.path.append("/usr/local/Cellar/opencv/2.4.12_2/lib/python2.7/site-packages")

import cv2
import os
import json
import os
import re
import time

targetFilePath = '/Users/gehongpeng/PycharmProjects/TableDetect/input/jpeg/'
resultFilePath = '/Users/gehongpeng/PycharmProjects/TableDetect/output/'
files = os.listdir(targetFilePath)
for file in files:
    jpg = re.compile("jpeg")
    if jpg.search(file):
        print file
        #
        img = cv2.imread(targetFilePath + file, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        #
        rsz = gray.copy()

        # Simple Thresholding
        # ret, bw = cv2.threshold(rsz, 120, 255, cv2.THRESH_BINARY_INV)

        # Adaptive Mean Thresholding
        # bw = cv2.adaptiveThreshold(rsz, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 23, 2)

        # Adaptive Gaussian Thresholding
        # bw = cv2.adaptiveThreshold(rsz, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 23, 2)

        # Otsu's thresholding after Gaussian filtering
        rsz = cv2.GaussianBlur(rsz, (5, 5), 0)
        ret, bw = cv2.threshold(rsz, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

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
        fileName = os.path.basename(targetFilePath + file)
        resultFile = os.path.splitext(fileName)[0]
        #cv2.imwrite(resultFilePath + resultFile + "_mask.jpg", mask)

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
            if (w <= 90) or (h <= 60):
                continue

            #
            sub_contours, sub_hierarchy = cv2.findContours(mask[y1:y1 + h, x1:x1 + w], cv2.RETR_CCOMP,
                                                           cv2.CHAIN_APPROX_SIMPLE)
            if len(sub_contours) <= 1:
                continue

            #
            contoursList.append((x1, y1, w, h))

        #
        #contoursList = sorted(contoursList, key=lambda x: (x[0], x[1]), reverse=False)
        contoursList = sorted(contoursList, key=lambda x: (x[1], x[0]), reverse=False)

        #
        tableList = []
        for contour in contoursList:
            #
            x1, y1, w, h = contour

            cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 1)

            #
            leftTop = {"X": x1, "Y": y1}
            rightBottom = {"X": x1 + w, "Y": y1 + h}
            table = {"LT": leftTop, "RB": rightBottom}

            #
            tableList.append(table)

        cv2.imwrite(resultFilePath + resultFile + "_contour.jpg", img)

        #
        #jsonstring = json.dumps(tableList, indent=4)
        #print(jsonstring)

        if len(tableList) == 2:
            #
            leftTop_x_1 = int(tableList[0]["LT"]["X"])
            leftTop_y_1 = int(tableList[0]["LT"]["Y"])
            rightBottom_x_1 = int(tableList[0]["RB"]["X"])
            rightBottom_y_1 = int(tableList[0]["RB"]["Y"])

            #
            leftTop_x_2 = int(tableList[1]["LT"]["X"])
            leftTop_y_2 = int(tableList[1]["LT"]["Y"])
            rightBottom_x_2 = int(tableList[1]["RB"]["X"])
            rightBottom_y_2 = int(tableList[1]["RB"]["Y"])


            #
            start_x = leftTop_x_1
            end_x = rightBottom_x_1
            start_y = leftTop_y_1
            end_y = rightBottom_y_1
            #
            cv2.imwrite(resultFilePath + "/1/" + resultFile + "_check.jpg", img[start_y:end_y, start_x:end_x])

            #
            start_x = leftTop_x_2
            end_x = rightBottom_x_2
            start_y = leftTop_y_2
            end_y = rightBottom_y_2
            cv2.imwrite(resultFilePath + "/2/" + resultFile + "_table.jpg", img[start_y:end_y, start_x:end_x])

        elif len(tableList) == 1:
            #
            leftTop_x_1 = int(tableList[0]["LT"]["X"])
            leftTop_y_1 = int(tableList[0]["LT"]["Y"])
            rightBottom_x_1 = int(tableList[0]["RB"]["X"])
            rightBottom_y_1 = int(tableList[0]["RB"]["Y"])

            #
            start_x = leftTop_x_1
            end_x = rightBottom_x_1
            start_y = leftTop_y_1
            end_y = rightBottom_y_1
            #
            cv2.imwrite(resultFilePath + "/2/" + resultFile + "_table.jpg", img[start_y:end_y, start_x:end_x])

            #print bw.shape
            h, w = bw.shape
            #
            start_x = leftTop_x_1
            end_x = int((leftTop_x_1 + (w * 0.4096)))

            end_y = start_y
            start_y = int(leftTop_y_1 - (h * 0.0744))
            #
            cv2.imwrite(resultFilePath + "/1/" + resultFile + "_check.jpg", img[start_y:end_y, start_x:end_x])
        else:
            print "wrong!!!"
    else:
        pass
