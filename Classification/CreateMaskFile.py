# _*_ coding= utf-8 _*_

import cv2
import numpy as np
import os
import glob
import csv
import re
import time

#指定する画像フォルダ
a = 1
files = os.listdir('./4_mask_train/')
for file in files:
    jpg = re.compile("jpeg")
    if jpg.search(file):
        print file
        os.rename('./4_mask_train/' + file, './4_mask_train/' + "table.jpg")
        time.sleep(2)

        #
        cmd = "sh /Users/gehongpeng/PycharmProjects/Classification/4_mask_train/run.sh"
        os.system(cmd)
        time.sleep(3)

        #
        desFileName = os.path.splitext(file)[0] + "_mask.jpg"
        os.rename('./4_mask_train/' + "_mask.jpg", './4_mask_train/test/' + desFileName)
    else:
        pass
