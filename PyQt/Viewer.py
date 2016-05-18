# -*- coding: utf-8 -*-

import sys
import os
import cv2
from PyQt4 import QtCore, QtGui

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

class ViewerDialog(QtGui.QDialog):
    def __init__(self):
        super(ViewerDialog, self).__init__()

        #
        self.setupUi(self)

    def setupUi(self, SettingDialog):
        SettingDialog.setObjectName(_fromUtf8("SettingDialog"))
        SettingDialog.resize(852, 708)
        self.horizontalLayoutWidget = QtGui.QWidget(SettingDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 651, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.BaseImageLabel = QtGui.QLabel(self.horizontalLayoutWidget)
        self.BaseImageLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.BaseImageLabel.setObjectName(_fromUtf8("BaseImageLabel"))
        self.horizontalLayout.addWidget(self.BaseImageLabel)
        self.BaseLineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.BaseLineEdit.setObjectName(_fromUtf8("BaseLineEdit"))
        self.horizontalLayout.addWidget(self.BaseLineEdit)
        self.BaseImageLoadPushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.BaseImageLoadPushButton.setObjectName(_fromUtf8("BaseImageLoadPushButton"))
        self.horizontalLayout.addWidget(self.BaseImageLoadPushButton)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(SettingDialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(680, 30, 160, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.OKPushButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.OKPushButton.setObjectName(_fromUtf8("OKPushButton"))
        self.horizontalLayout_2.addWidget(self.OKPushButton)
        self.CancelPushButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.CancelPushButton.setObjectName(_fromUtf8("CancelPushButton"))
        self.horizontalLayout_2.addWidget(self.CancelPushButton)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(SettingDialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 56, 651, 41))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.TargetBaseImageLabel = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.TargetBaseImageLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TargetBaseImageLabel.setObjectName(_fromUtf8("TargetBaseImageLabel"))
        self.horizontalLayout_3.addWidget(self.TargetBaseImageLabel)
        self.TargetLineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget_3)
        self.TargetLineEdit.setObjectName(_fromUtf8("TargetLineEdit"))
        self.horizontalLayout_3.addWidget(self.TargetLineEdit)
        self.TargetImageLoadPushButton = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.TargetImageLoadPushButton.setObjectName(_fromUtf8("TargetImageLoadPushButton"))
        self.horizontalLayout_3.addWidget(self.TargetImageLoadPushButton)
        self.ImageLabel = QtGui.QLabel(SettingDialog)
        self.ImageLabel.setGeometry(QtCore.QRect(10, 120, 831, 571))
        self.ImageLabel.setFrameShape(QtGui.QFrame.Panel)
        self.ImageLabel.setText(_fromUtf8(""))
        self.ImageLabel.setObjectName(_fromUtf8("ImageLabel"))

        self.retranslateUi(SettingDialog)
        QtCore.QMetaObject.connectSlotsByName(SettingDialog)

    def retranslateUi(self, SettingDialog):
        # 禁止拉伸窗口大小
        SettingDialog.setFixedSize(SettingDialog.width(), SettingDialog.height())

        SettingDialog.setWindowTitle(_translate("SettingDialog", "Viewer", None))
        self.BaseImageLabel.setText(_translate("SettingDialog", "Base image file path  ", None))
        self.BaseImageLoadPushButton.setText(_translate("SettingDialog", "...", None))
        self.OKPushButton.setText(_translate("SettingDialog", "OK", None))
        self.CancelPushButton.setText(_translate("SettingDialog", "Cancel", None))
        self.TargetBaseImageLabel.setText(_translate("SettingDialog", "Target image file path", None))
        self.TargetImageLoadPushButton.setText(_translate("SettingDialog", "...", None))

        # Base Load PushButton event
        self.BaseImageLoadPushButton.clicked.connect(self.imagefileLoad)

        # Target Load PushButton event
        self.TargetImageLoadPushButton.clicked.connect(self.imagefileLoad)

        # OK PushButton event
        self.OKPushButton.clicked.connect(self.okPushButtonClick)

        # Cancel PushButton event
        self.CancelPushButton.clicked.connect(self.cancelPushButtonClick)

    def imagefileLoad(self):
        #
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', os.path.expanduser('~') + '/Desktop')

        if self.sender().objectName() == 'BaseImageLoadPushButton':
            #
            self.BaseLineEdit.setText(filename)
        elif self.sender().objectName() == 'TargetImageLoadPushButton':
            #
            self.TargetLineEdit.setText(filename)

            #
            # self.local_image = QtGui.QImage(self.lineEdit.text())
            # self.pixMapItem = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(self.local_image), None, self.local_scene)

    def okPushButtonClick(self):

        imgbase = cv2.imread(str(self.BaseLineEdit.text()))
        imgtarget = cv2.imread(str(self.TargetLineEdit.text()))
        dsttest = cv2.addWeighted(imgbase, 0.5, imgtarget, 0.5, 0)
        cv2.imwrite('./tmp.jpg', dsttest)

        pixmap = QtGui.QPixmap('./tmp.jpg')
        self.ImageLabel.setPixmap(pixmap)
        os.remove('./tmp.jpg')

    def cancelPushButtonClick(self):
        self.reject()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = ViewerDialog()
    ex.show()
    sys.exit(app.exec_())
