# -*- coding: utf-8 -*-

import sys
import cv2
import os
import glob
import numpy as np
from PyQt4 import QtCore, QtGui
from SettingFromImageDialog import SettingFromImageDialog
from ProgressWidget import ProcessingWidget

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class ImageTransformation(QtGui.QMainWindow):
    def __init__(self):
        super(ImageTransformation, self).__init__()

        #
        self.settingImageDialog = None
        self.settingFlag = ''
        self.targetrows = 0
        self.targetcols = 0

        #
        self.processingWidget = None

        #
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(796, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.BaseGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.BaseGroupBox.setGeometry(QtCore.QRect(20, 10, 361, 291))
        self.BaseGroupBox.setObjectName(_fromUtf8("BaseGroupBox"))
        self.BasePointsDirectionGroupBox = QtGui.QGroupBox(self.BaseGroupBox)
        self.BasePointsDirectionGroupBox.setGeometry(QtCore.QRect(10, 80, 101, 191))
        self.BasePointsDirectionGroupBox.setObjectName(_fromUtf8("BasePointsDirectionGroupBox"))
        self.verticalLayoutWidget = QtGui.QWidget(self.BasePointsDirectionGroupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 81, 181))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.BasePointDirectionVerticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.BasePointDirectionVerticalLayout.setObjectName(_fromUtf8("BasePointDirectionVerticalLayout"))
        self.BaseLeftTopLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.BaseLeftTopLabel.setObjectName(_fromUtf8("BaseLeftTopLabel"))
        self.BasePointDirectionVerticalLayout.addWidget(self.BaseLeftTopLabel)
        self.BaseRightTopLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.BaseRightTopLabel.setObjectName(_fromUtf8("BaseRightTopLabel"))
        self.BasePointDirectionVerticalLayout.addWidget(self.BaseRightTopLabel)
        self.BaseRightBottomLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.BaseRightBottomLabel.setObjectName(_fromUtf8("BaseRightBottomLabel"))
        self.BasePointDirectionVerticalLayout.addWidget(self.BaseRightBottomLabel)
        self.BaseLeftBottomLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.BaseLeftBottomLabel.setObjectName(_fromUtf8("BaseLeftBottomLabel"))
        self.BasePointDirectionVerticalLayout.addWidget(self.BaseLeftBottomLabel)
        self.BasePointsXGroupBox = QtGui.QGroupBox(self.BaseGroupBox)
        self.BasePointsXGroupBox.setGeometry(QtCore.QRect(130, 80, 101, 191))
        self.BasePointsXGroupBox.setObjectName(_fromUtf8("BasePointsXGroupBox"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.BasePointsXGroupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 81, 181))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.BasePointXVerticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.BasePointXVerticalLayout.setObjectName(_fromUtf8("BasePointXVerticalLayout"))
        self.BaseLeftTopXLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.BaseLeftTopXLineEdit.setObjectName(_fromUtf8("BaseLeftTopXLineEdit"))
        self.BasePointXVerticalLayout.addWidget(self.BaseLeftTopXLineEdit)
        self.BaseRightTopXLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.BaseRightTopXLineEdit.setObjectName(_fromUtf8("BaseRightTopXLineEdit"))
        self.BasePointXVerticalLayout.addWidget(self.BaseRightTopXLineEdit)
        self.BaseRightBottomXLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.BaseRightBottomXLineEdit.setObjectName(_fromUtf8("BaseRightBottomXLineEdit"))
        self.BasePointXVerticalLayout.addWidget(self.BaseRightBottomXLineEdit)
        self.BaseLeftBottomXLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.BaseLeftBottomXLineEdit.setObjectName(_fromUtf8("BaseLeftBottomXLineEdit"))
        self.BasePointXVerticalLayout.addWidget(self.BaseLeftBottomXLineEdit)
        self.BasePointsYGroupBox = QtGui.QGroupBox(self.BaseGroupBox)
        self.BasePointsYGroupBox.setGeometry(QtCore.QRect(250, 80, 101, 191))
        self.BasePointsYGroupBox.setObjectName(_fromUtf8("BasePointsYGroupBox"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.BasePointsYGroupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 81, 181))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.BasePointYVerticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.BasePointYVerticalLayout.setObjectName(_fromUtf8("BasePointYVerticalLayout"))
        self.BaseLeftTopYLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.BaseLeftTopYLineEdit.setObjectName(_fromUtf8("BaseLeftTopYLineEdit"))
        self.BasePointYVerticalLayout.addWidget(self.BaseLeftTopYLineEdit)
        self.BaseRightTopYLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.BaseRightTopYLineEdit.setObjectName(_fromUtf8("BaseRightTopYLineEdit"))
        self.BasePointYVerticalLayout.addWidget(self.BaseRightTopYLineEdit)
        self.BaseRightBottomYLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.BaseRightBottomYLineEdit.setObjectName(_fromUtf8("BaseRightBottomYLineEdit"))
        self.BasePointYVerticalLayout.addWidget(self.BaseRightBottomYLineEdit)
        self.BaseLeftBottomYLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.BaseLeftBottomYLineEdit.setObjectName(_fromUtf8("BaseLeftBottomYLineEdit"))
        self.BasePointYVerticalLayout.addWidget(self.BaseLeftBottomYLineEdit)
        self.BaseSettingPushButton = QtGui.QPushButton(self.BaseGroupBox)
        self.BaseSettingPushButton.setGeometry(QtCore.QRect(10, 20, 341, 41))
        self.BaseSettingPushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BaseSettingPushButton.setObjectName(_fromUtf8("BaseSettingPushButton"))
        self.TargetGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.TargetGroupBox.setGeometry(QtCore.QRect(410, 10, 361, 291))
        self.TargetGroupBox.setObjectName(_fromUtf8("TargetGroupBox"))
        self.TargetPointsDirectionGroupBox = QtGui.QGroupBox(self.TargetGroupBox)
        self.TargetPointsDirectionGroupBox.setGeometry(QtCore.QRect(10, 80, 101, 191))
        self.TargetPointsDirectionGroupBox.setObjectName(_fromUtf8("TargetPointsDirectionGroupBox"))
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.TargetPointsDirectionGroupBox)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 81, 181))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.TargetPointDirectionVerticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.TargetPointDirectionVerticalLayout.setObjectName(_fromUtf8("TargetPointDirectionVerticalLayout"))
        self.TargetLeftTopLabel = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.TargetLeftTopLabel.setObjectName(_fromUtf8("TargetLeftTopLabel"))
        self.TargetPointDirectionVerticalLayout.addWidget(self.TargetLeftTopLabel)
        self.TargetRightTopLabel = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.TargetRightTopLabel.setObjectName(_fromUtf8("TargetRightTopLabel"))
        self.TargetPointDirectionVerticalLayout.addWidget(self.TargetRightTopLabel)
        self.TargetRightBottomLabel = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.TargetRightBottomLabel.setObjectName(_fromUtf8("TargetRightBottomLabel"))
        self.TargetPointDirectionVerticalLayout.addWidget(self.TargetRightBottomLabel)
        self.TargetLeftBottomLabel = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.TargetLeftBottomLabel.setObjectName(_fromUtf8("TargetLeftBottomLabel"))
        self.TargetPointDirectionVerticalLayout.addWidget(self.TargetLeftBottomLabel)
        self.TargetPointsXGroupBox = QtGui.QGroupBox(self.TargetGroupBox)
        self.TargetPointsXGroupBox.setGeometry(QtCore.QRect(130, 80, 101, 191))
        self.TargetPointsXGroupBox.setObjectName(_fromUtf8("TargetPointsXGroupBox"))
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.TargetPointsXGroupBox)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 81, 181))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.TargetPointXVerticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.TargetPointXVerticalLayout.setObjectName(_fromUtf8("TargetPointXVerticalLayout"))
        self.TargetLeftTopXLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.TargetLeftTopXLineEdit.setObjectName(_fromUtf8("TargetLeftTopXLineEdit"))
        self.TargetPointXVerticalLayout.addWidget(self.TargetLeftTopXLineEdit)
        self.TargetRightTopXLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.TargetRightTopXLineEdit.setObjectName(_fromUtf8("TargetRightTopXLineEdit"))
        self.TargetPointXVerticalLayout.addWidget(self.TargetRightTopXLineEdit)
        self.TargetRightBottomXLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.TargetRightBottomXLineEdit.setObjectName(_fromUtf8("TargetRightBottomXLineEdit"))
        self.TargetPointXVerticalLayout.addWidget(self.TargetRightBottomXLineEdit)
        self.TargetLeftBottomXLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_5)
        self.TargetLeftBottomXLineEdit.setObjectName(_fromUtf8("TargetLeftBottomXLineEdit"))
        self.TargetPointXVerticalLayout.addWidget(self.TargetLeftBottomXLineEdit)
        self.TargetPointsYGroupBox = QtGui.QGroupBox(self.TargetGroupBox)
        self.TargetPointsYGroupBox.setGeometry(QtCore.QRect(250, 80, 101, 191))
        self.TargetPointsYGroupBox.setObjectName(_fromUtf8("TargetPointsYGroupBox"))
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.TargetPointsYGroupBox)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 10, 81, 181))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.TargetPointYVerticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.TargetPointYVerticalLayout.setObjectName(_fromUtf8("TargetPointYVerticalLayout"))
        self.TargetLeftTopYLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.TargetLeftTopYLineEdit.setObjectName(_fromUtf8("TargetLeftTopYLineEdit"))
        self.TargetPointYVerticalLayout.addWidget(self.TargetLeftTopYLineEdit)
        self.TargetRightTopYLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.TargetRightTopYLineEdit.setObjectName(_fromUtf8("TargetRightTopYLineEdit"))
        self.TargetPointYVerticalLayout.addWidget(self.TargetRightTopYLineEdit)
        self.TargetRightBottomYLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.TargetRightBottomYLineEdit.setObjectName(_fromUtf8("TargetRightBottomYLineEdit"))
        self.TargetPointYVerticalLayout.addWidget(self.TargetRightBottomYLineEdit)
        self.TargetLeftBottomYLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.TargetLeftBottomYLineEdit.setObjectName(_fromUtf8("TargetLeftBottomYLineEdit"))
        self.TargetPointYVerticalLayout.addWidget(self.TargetLeftBottomYLineEdit)
        self.TargetSettingPushButton = QtGui.QPushButton(self.TargetGroupBox)
        self.TargetSettingPushButton.setGeometry(QtCore.QRect(10, 20, 341, 41))
        self.TargetSettingPushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TargetSettingPushButton.setObjectName(_fromUtf8("TargetSettingPushButton"))
        self.TargetGroupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.TargetGroupBox_2.setGeometry(QtCore.QRect(20, 310, 751, 80))
        self.TargetGroupBox_2.setObjectName(_fromUtf8("TargetGroupBox_2"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.TargetGroupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 731, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.TargetPathLabel = QtGui.QLabel(self.horizontalLayoutWidget)
        self.TargetPathLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TargetPathLabel.setObjectName(_fromUtf8("TargetPathLabel"))
        self.horizontalLayout.addWidget(self.TargetPathLabel)
        self.TargetPathLineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.TargetPathLineEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.TargetPathLineEdit.setObjectName(_fromUtf8("TargetPathLineEdit"))
        self.horizontalLayout.addWidget(self.TargetPathLineEdit)
        self.DirectoryPushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.DirectoryPushButton.setObjectName(_fromUtf8("DirectoryPushButton"))
        self.horizontalLayout.addWidget(self.DirectoryPushButton)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(320, 400, 160, 51))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.RunPushButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.RunPushButton.setMaximumSize(QtCore.QSize(16777215, 23))
        self.RunPushButton.setObjectName(_fromUtf8("RunPushButton"))
        self.horizontalLayout_2.addWidget(self.RunPushButton)
        self.CancelPushButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.CancelPushButton.setObjectName(_fromUtf8("CancelPushButton"))
        self.horizontalLayout_2.addWidget(self.CancelPushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # 禁止拉伸窗口大小
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())

        MainWindow.setWindowTitle(_translate("MainWindow", "Image Transformation", None))
        self.BaseGroupBox.setTitle(_translate("MainWindow", "Base image coordinates setting", None))
        self.BasePointsDirectionGroupBox.setTitle(_translate("MainWindow", "Points direction", None))
        self.BaseLeftTopLabel.setText(_translate("MainWindow", "Left-Top", None))
        self.BaseRightTopLabel.setText(_translate("MainWindow", "Right-Top", None))
        self.BaseRightBottomLabel.setText(_translate("MainWindow", "Right-Bottom", None))
        self.BaseLeftBottomLabel.setText(_translate("MainWindow", "Left-Bottom", None))
        self.BasePointsXGroupBox.setTitle(_translate("MainWindow", "X", None))
        self.BasePointsYGroupBox.setTitle(_translate("MainWindow", "Y", None))
        self.BaseSettingPushButton.setText(_translate("MainWindow", "Setting from image", None))
        self.TargetGroupBox.setTitle(_translate("MainWindow", "Target image coordinates setting", None))
        self.TargetPointsDirectionGroupBox.setTitle(_translate("MainWindow", "Points direction", None))
        self.TargetLeftTopLabel.setText(_translate("MainWindow", "Left-Top", None))
        self.TargetRightTopLabel.setText(_translate("MainWindow", "Right-Top", None))
        self.TargetRightBottomLabel.setText(_translate("MainWindow", "Right-Bottom", None))
        self.TargetLeftBottomLabel.setText(_translate("MainWindow", "Left-Bottom", None))
        self.TargetPointsXGroupBox.setTitle(_translate("MainWindow", "X", None))
        self.TargetPointsYGroupBox.setTitle(_translate("MainWindow", "Y", None))
        self.TargetSettingPushButton.setText(_translate("MainWindow", "Setting from image", None))
        self.TargetGroupBox_2.setTitle(_translate("MainWindow", "Target files", None))
        self.TargetPathLabel.setText(_translate("MainWindow", "Path:", None))
        self.DirectoryPushButton.setText(_translate("MainWindow", "Directory", None))
        self.RunPushButton.setText(_translate("MainWindow", "Run", None))
        self.CancelPushButton.setText(_translate("MainWindow", "Cancel", None))

        self.BaseSettingPushButton.clicked.connect(self.baseSettingPushButtonOnClick)
        self.TargetSettingPushButton.clicked.connect(self.baseSettingPushButtonOnClick)
        self.DirectoryPushButton.clicked.connect(self.directoryButtonOnClick)
        self.RunPushButton.clicked.connect(self.runButtonOnClick)

    def baseSettingPushButtonOnClick(self):
        # Show image setting dialog
        self.settingImageDialog = SettingFromImageDialog()
        self.settingImageDialog.show()
        self.settingImageDialog.raise_()

        # Connect event function
        self.settingImageDialog.OKPushButton.clicked.connect(self.coordinateValueSet)

        #print self.sender().objectName()

        if self.sender().objectName() == 'BaseSettingPushButton':
            self.settingFlag = "Base"
        elif self.sender().objectName() == 'TargetSettingPushButton':
            self.settingFlag = "Target"

    def coordinateValueSet(self):
        if self.settingFlag == 'Base':
            self.BaseLeftTopXLineEdit.setText(self.settingImageDialog.LeftTopXLineEdit.text())
            self.BaseLeftTopYLineEdit.setText(self.settingImageDialog.LeftTopYLineEdit.text())

            self.BaseRightTopXLineEdit.setText(self.settingImageDialog.RightTopXLineEdit.text())
            self.BaseRightTopYLineEdit.setText(self.settingImageDialog.RightTopYLineEdit.text())

            self.BaseRightBottomXLineEdit.setText(self.settingImageDialog.RightBottomXLineEdit.text())
            self.BaseRightBottomYLineEdit.setText(self.settingImageDialog.RightBottomYLineEdit.text())

            self.BaseLeftBottomXLineEdit.setText(self.settingImageDialog.LeftBottomXLineEdit.text())
            self.BaseLeftBottomYLineEdit.setText(self.settingImageDialog.LeftBottomYLineEdit.text())

            self.targetrows = self.settingImageDialog.rows
            self.targetcols = self.settingImageDialog.cols

        elif self.settingFlag == 'Target':
            self.TargetLeftTopXLineEdit.setText(self.settingImageDialog.LeftTopXLineEdit.text())
            self.TargetLeftTopYLineEdit.setText(self.settingImageDialog.LeftTopYLineEdit.text())

            self.TargetRightTopXLineEdit.setText(self.settingImageDialog.RightTopXLineEdit.text())
            self.TargetRightTopYLineEdit.setText(self.settingImageDialog.RightTopYLineEdit.text())

            self.TargetRightBottomXLineEdit.setText(self.settingImageDialog.RightBottomXLineEdit.text())
            self.TargetRightBottomYLineEdit.setText(self.settingImageDialog.RightBottomYLineEdit.text())

            self.TargetLeftBottomXLineEdit.setText(self.settingImageDialog.LeftBottomXLineEdit.text())
            self.TargetLeftBottomYLineEdit.setText(self.settingImageDialog.LeftBottomYLineEdit.text())

    def directoryButtonOnClick(self):
        self.TargetPathLineEdit.setText(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))

    def runButtonOnClick(self):
        #
        targetPoint = np.float32([[self.TargetLeftTopXLineEdit.text(), self.TargetLeftTopYLineEdit.text()],
                                  [self.TargetRightTopXLineEdit.text(), self.TargetRightTopYLineEdit.text()],
                                  [self.TargetRightBottomXLineEdit.text(), self.TargetRightBottomYLineEdit.text()],
                                  [self.TargetLeftBottomXLineEdit.text(), self.TargetLeftBottomYLineEdit.text()]])
        basePoint = np.float32([[self.BaseLeftTopXLineEdit.text(), self.BaseLeftTopYLineEdit.text()],
                                [self.BaseRightTopXLineEdit.text(), self.BaseRightTopYLineEdit.text()],
                                [self.BaseRightBottomXLineEdit.text(), self.BaseRightBottomYLineEdit.text()],
                                [self.BaseLeftBottomXLineEdit.text(), self.BaseLeftBottomYLineEdit.text()]])

        #
        M = cv2.getPerspectiveTransform(targetPoint, basePoint)

        # Create output directory
        resultPath = str(self.TargetPathLineEdit.text() + '\\result')
        if not os.path.exists(resultPath):
            os.makedirs(resultPath)

        #
        files = glob.glob(str(self.TargetPathLineEdit.text() + '\\*.*'))

        #
        self.processingWidget = ProcessingWidget()
        self.processingWidget.progressBar.setMaximum(len(files))
        self.processingWidget.progressBar.setValue(0)
        self.processingWidget.show()

        #
        progressBarCounter = 0
        for file in files:
            #
            baseFilename = os.path.basename(file)
            spliteFilename = os.path.splitext(baseFilename)

            #
            img = cv2.imread(file)
            dst = cv2.warpPerspective(img, M, (self.targetcols, self.targetrows))
            cv2.imwrite('{0}\\{1}_transformed{2}'.format(resultPath, spliteFilename[0], spliteFilename[1]), dst)

            progressBarCounter += 1
            self.processingWidget.progressBar.setValue(progressBarCounter)

        #
        self.processingWidget.InformationLabel.setText("Processing Completed!")

        # Messsage Box
        #msg = QtGui.QMessageBox()
        #msg.setIcon(QtGui.QMessageBox.Information)
        #msg.setText("Processing Completed!")
        #msg.setWindowTitle("Information")
        #msg.setStandardButtons(QtGui.QMessageBox.Ok)
        #msg.exec_()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = ImageTransformation()
    ex.show()
    sys.exit(app.exec_())
