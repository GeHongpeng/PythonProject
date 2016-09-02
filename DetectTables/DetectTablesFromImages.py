# _*_ coding= utf-8 _*_

import sys
sys.path.append("/usr/local/Cellar/numpy/1.11.0/lib/python2.7/site-packages")
sys.path.append("/usr/local/Cellar/opencv/2.4.12_2/lib/python2.7/site-packages")

import numpy as np
import cv2
import json
import os
import re

#
targetFilePath = '/Users/gehongpeng/PycharmProjects/TableDetect/input/test/'
resultFilePath = '/Users/gehongpeng/PycharmProjects/TableDetect/data/'


def comparator(tuple1, tuple2):
    x = 0
    y = 1
    if tuple2[y] < tuple1[y]:
        return 1
    elif tuple2[y] > tuple1[y]:
        return -1
    else:
        if tuple2[x] < tuple1[x]:
            return 1
        elif tuple2[x] > tuple1[x]:
            return -1
        else:
            return 0


def isOverlap(rect1, rect2, imageWidth, imageHeight):
    # index info
    x = 0
    y = 1
    w = 2
    h = 3

    #
    targetUnit = np.array([1])

    # check x axis
    rectArrayX1 = np.zeros(imageWidth)
    rectArrayX2 = np.zeros(imageWidth)
    rectArrayX1[rect1[x]:rect1[x]+rect1[w]] = 1
    rectArrayX2[rect2[x]:rect2[x]+rect2[w]] = 1
    xAxisOverlapped = np.in1d(targetUnit, np.logical_and(rectArrayX1, rectArrayX2))[0]

    # check y axis
    rectArrayY1 = np.zeros(imageHeight)
    rectArrayY2 = np.zeros(imageHeight)
    rectArrayY1[rect1[y]:rect1[y]+rect1[h]] = 1
    rectArrayY2[rect2[y]:rect2[y]+rect2[h]] = 1
    yAxisOverlapped = np.in1d(targetUnit, np.logical_and(rectArrayY1, rectArrayY2))[0]

    #
    return xAxisOverlapped & yAxisOverlapped

#
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
        #ret, bw = cv2.threshold(rsz, 120, 255, cv2.THRESH_BINARY_INV)

        # Adaptive Mean Thresholding
        bw = cv2.adaptiveThreshold(rsz, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 23, 2)

        # Adaptive Gaussian Thresholding
        #bw = cv2.adaptiveThreshold(rsz, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 23, 2)

        # Otsu's thresholding after Gaussian filtering
        #rsz = cv2.GaussianBlur(rsz, (5, 5), 0)
        #ret, bw = cv2.threshold(rsz, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

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

        # create mask image
        mask = horizontal + vertical

        # save mask image
        fileName = os.path.basename(targetFilePath + file)
        resultFile = os.path.splitext(fileName)[0]
        #cv2.imwrite(resultFilePath + resultFile + "_mask.jpg", mask)

        # create joint points image
        jointPoints = cv2.bitwise_and(horizontal, vertical)
        #cv2.imwrite(resultFilePath + resultFile + "_jointPoints.jpg", jointPoints)

        # find Contours
        contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #
        # contours = sorted(contours, key=cv2.contourArea, reverse=True)

        # find tables
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
            sub_contours, sub_hierarchy = cv2.findContours(mask[y1:y1 + h, x1:x1 + w], cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
            if len(sub_contours) <= 1:
                continue

            #
            contoursList.append((x1, y1, w, h))

        # sort contour list
        #contoursList = sorted(contoursList, key=lambda x: (x[0], x[1]), reverse=False)
        #contoursList = sorted(contoursList, key=lambda x: (x[1], x[0]), reverse=False)
        contoursList.sort(comparator)


        # merge
        mergedContoursList = []
        height, width = bw.shape
        for i, p in enumerate(contoursList):
            #
            if len(mergedContoursList) == 0:
                mergedContoursList.append(contoursList[i])
                continue

            #
            flag = False
            xi, yi, wi, hi = contoursList[i]
            for j, q in enumerate(mergedContoursList):
                flag = isOverlap(mergedContoursList[j], contoursList[i], width, height)
                if flag == False:
                    continue

                #
                xj, yj, wj, hj = mergedContoursList[j]
                #
                xNew = min(xi, xj)
                yNew = min(yi, yj)
                wNew = max(xi+wi, xj+wj) - xNew
                hNew = max(yi+hi, yj+hj) - yNew
                #
                mergedContoursList.pop(j)
                #
                mergedContoursList.append((xNew, yNew, wNew, hNew))
                break
            #
            if flag == False:
                mergedContoursList.append(contoursList[i])


        # draw rectangles on img
        contourImage = img.copy()
        for contour in mergedContoursList:
            #
            x1, y1, w, h = contour
            cv2.rectangle(contourImage, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 1)
        # save contour image
        contourResultPath = resultFilePath + "contour/"
        if not os.path.exists(contourResultPath):
            os.makedirs(contourResultPath)
        cv2.imwrite(contourResultPath + resultFile + "_contour.jpg", contourImage)

        # print json structure
        tableList = []
        for contour in mergedContoursList:
            #
            x1, y1, w, h = contour

            #
            leftTop = {"X": x1, "Y": y1}
            rightBottom = {"X": x1 + w, "Y": y1 + h}
            table = {"LT": leftTop, "RB": rightBottom}
            #
            tableList.append(table)
        #
        jsonString = json.dumps(tableList, indent=4)
        #print(jsonString)

        #
        targetTableList = json.loads(jsonString)
        for i, targetTable in enumerate(targetTableList):
            #
            organizationId = resultFile.split('-')[0]
            documentId = resultFile.split('-')[1]
            #
            #resultPath = resultFilePath + "%03d/" % (i+1)
            resultPath = '{0}{1}/{2}/{3}'.format(resultFilePath, organizationId, documentId, "table%03d/" % (i+1))
            if not os.path.exists(resultPath):
                os.makedirs(resultPath)

            #
            cv2.imwrite(resultPath + resultFile + "_table%03d.jpg" % (i+1),
                        img[targetTable["LT"]["Y"]:targetTable["RB"]["Y"], targetTable["LT"]["X"]:targetTable["RB"]["X"]])

        """
        # crop tables from img
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
            cv2.imwrite(resultFilePath + "/1/" + resultFile + "_check.jpg", img[leftTop_y_1:rightBottom_y_1, leftTop_x_1:rightBottom_x_1])
            #
            cv2.imwrite(resultFilePath + "/2/" + resultFile + "_table.jpg", img[leftTop_y_2:rightBottom_y_2, leftTop_x_2:rightBottom_x_2])

        elif len(tableList) == 1:
            #
            leftTop_x_1 = int(tableList[0]["LT"]["X"])
            leftTop_y_1 = int(tableList[0]["LT"]["Y"])
            rightBottom_x_1 = int(tableList[0]["RB"]["X"])
            rightBottom_y_1 = int(tableList[0]["RB"]["Y"])

            #
            cv2.imwrite(resultFilePath + "/2/" + resultFile + "_table.jpg", img[leftTop_y_1:rightBottom_y_1, leftTop_x_1:rightBottom_x_1])

            #
            h, w = bw.shape
            #
            start_x = leftTop_x_1
            end_x = int((leftTop_x_1 + (w * 0.4096)))

            end_y = leftTop_y_1
            start_y = int(leftTop_y_1 - (h * 0.0744))
            #
            cv2.imwrite(resultFilePath + "/1/" + resultFile + "_check.jpg", img[start_y:end_y, start_x:end_x])
        else:
            print "wrong!!!"
        """
    else:
        pass
