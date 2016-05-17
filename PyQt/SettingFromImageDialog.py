# -*- coding: utf-8 -*-

import sys
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

class SettingFromImageDialog(QtGui.QDialog):
    def __init__(self):
        super(SettingFromImageDialog, self).__init__()
        self.setupUi(self)

    def setupUi(self, SettingDialog):
        SettingDialog.setObjectName(_fromUtf8("SettingDialog"))
        SettingDialog.resize(1211, 643)

        self.ImageGraphicsView = QtGui.QGraphicsView(SettingDialog)
        self.ImageGraphicsView.setGeometry(QtCore.QRect(10, 60, 811, 561))
        self.ImageGraphicsView.setObjectName(_fromUtf8("ImageGraphicsView"))

        self.local_image = QtGui.QImage('')
        self.local_scene = QtGui.QGraphicsScene()
        self.image_format = self.local_image.format()

        self.pixMapItem = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(self.local_image), None, self.local_scene)
        self.ImageGraphicsView.setScene(self.local_scene)
        # self.pixMapItem.mousePressEvent = self.pixelSelect

        self.horizontalLayoutWidget = QtGui.QWidget(SettingDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 651, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.BaseImageLabel = QtGui.QLabel(self.horizontalLayoutWidget)
        self.BaseImageLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.BaseImageLabel.setObjectName(_fromUtf8("BaseImageLabel"))
        self.horizontalLayout.addWidget(self.BaseImageLabel)
        self.lineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.ImageLoadPushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.ImageLoadPushButton.setObjectName(_fromUtf8("ImageLoadPushButton"))
        self.horizontalLayout.addWidget(self.ImageLoadPushButton)
        self.PointsYGroupBox = QtGui.QGroupBox(SettingDialog)
        self.PointsYGroupBox.setGeometry(QtCore.QRect(1090, 60, 101, 191))
        self.PointsYGroupBox.setObjectName(_fromUtf8("PointsYGroupBox"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.PointsYGroupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 81, 181))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.PointYVerticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.PointYVerticalLayout.setObjectName(_fromUtf8("PointYVerticalLayout"))
        self.LeftTopYLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.LeftTopYLineEdit.setObjectName(_fromUtf8("LeftTopYLineEdit"))
        self.PointYVerticalLayout.addWidget(self.LeftTopYLineEdit)
        self.RightTopYLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.RightTopYLineEdit.setObjectName(_fromUtf8("RightTopYLineEdit"))
        self.PointYVerticalLayout.addWidget(self.RightTopYLineEdit)
        self.RightBottomYLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.RightBottomYLineEdit.setObjectName(_fromUtf8("RightBottomYLineEdit"))
        self.PointYVerticalLayout.addWidget(self.RightBottomYLineEdit)
        self.LeftBottomYLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.LeftBottomYLineEdit.setObjectName(_fromUtf8("LeftBottomYLineEdit"))
        self.PointYVerticalLayout.addWidget(self.LeftBottomYLineEdit)
        self.PointsDirectionGroupBox = QtGui.QGroupBox(SettingDialog)
        self.PointsDirectionGroupBox.setGeometry(QtCore.QRect(850, 60, 101, 191))
        self.PointsDirectionGroupBox.setObjectName(_fromUtf8("PointsDirectionGroupBox"))
        self.verticalLayoutWidget = QtGui.QWidget(self.PointsDirectionGroupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 81, 181))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.PointDirectionVerticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.PointDirectionVerticalLayout.setObjectName(_fromUtf8("PointDirectionVerticalLayout"))
        self.LeftTopLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.LeftTopLabel.setObjectName(_fromUtf8("LeftTopLabel"))
        self.PointDirectionVerticalLayout.addWidget(self.LeftTopLabel)
        self.RightTopLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.RightTopLabel.setObjectName(_fromUtf8("RightTopLabel"))
        self.PointDirectionVerticalLayout.addWidget(self.RightTopLabel)
        self.RightBottomLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.RightBottomLabel.setObjectName(_fromUtf8("RightBottomLabel"))
        self.PointDirectionVerticalLayout.addWidget(self.RightBottomLabel)
        self.LeftBottomLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.LeftBottomLabel.setObjectName(_fromUtf8("LeftBottomLabel"))
        self.PointDirectionVerticalLayout.addWidget(self.LeftBottomLabel)
        self.PointsXGroupBox = QtGui.QGroupBox(SettingDialog)
        self.PointsXGroupBox.setGeometry(QtCore.QRect(970, 60, 101, 191))
        self.PointsXGroupBox.setObjectName(_fromUtf8("PointsXGroupBox"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.PointsXGroupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 81, 181))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.PointXVerticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.PointXVerticalLayout.setObjectName(_fromUtf8("PointXVerticalLayout"))
        self.LeftTopXLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.LeftTopXLineEdit.setObjectName(_fromUtf8("LeftTopXLineEdit"))
        self.PointXVerticalLayout.addWidget(self.LeftTopXLineEdit)
        self.RightTopXLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.RightTopXLineEdit.setObjectName(_fromUtf8("RightTopXLineEdit"))
        self.PointXVerticalLayout.addWidget(self.RightTopXLineEdit)
        self.RightBottomXLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.RightBottomXLineEdit.setObjectName(_fromUtf8("RightBottomXLineEdit"))
        self.PointXVerticalLayout.addWidget(self.RightBottomXLineEdit)
        self.LeftBottomXLineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.LeftBottomXLineEdit.setObjectName(_fromUtf8("LeftBottomXLineEdit"))
        self.PointXVerticalLayout.addWidget(self.LeftBottomXLineEdit)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(SettingDialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(900, 320, 239, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.OKPushButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.OKPushButton.setObjectName(_fromUtf8("OKPushButton"))
        self.horizontalLayout_2.addWidget(self.OKPushButton)
        self.CancelPushButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.CancelPushButton.setObjectName(_fromUtf8("CancelPushButton"))
        self.horizontalLayout_2.addWidget(self.CancelPushButton)
        self.ResetPushButton = QtGui.QPushButton(SettingDialog)
        self.ResetPushButton.setGeometry(QtCore.QRect(980, 270, 75, 31))
        self.ResetPushButton.setObjectName(_fromUtf8("ResetPushButton"))

        self.retranslateUi(SettingDialog)
        QtCore.QMetaObject.connectSlotsByName(SettingDialog)

        self.show()

    def retranslateUi(self, SettingDialog):
        # 禁止拉伸窗口大小
        SettingDialog.setFixedSize(SettingDialog.width(), SettingDialog.height())

        SettingDialog.setWindowTitle(_translate("SettingDialog", "Setting from image", None))
        self.BaseImageLabel.setText(_translate("SettingDialog", "Base image file path", None))
        self.ImageLoadPushButton.setText(_translate("SettingDialog", "Load", None))
        self.PointsYGroupBox.setTitle(_translate("SettingDialog", "Y", None))
        self.PointsDirectionGroupBox.setTitle(_translate("SettingDialog", "Points direction", None))
        self.LeftTopLabel.setText(_translate("SettingDialog", "Left-Top", None))
        self.RightTopLabel.setText(_translate("SettingDialog", "Right-Top", None))
        self.RightBottomLabel.setText(_translate("SettingDialog", "Right-Bottom", None))
        self.LeftBottomLabel.setText(_translate("SettingDialog", "Left-Bottom", None))
        self.PointsXGroupBox.setTitle(_translate("SettingDialog", "X", None))
        self.OKPushButton.setText(_translate("SettingDialog", "OK", None))
        self.CancelPushButton.setText(_translate("SettingDialog", "Cancel", None))
        self.ResetPushButton.setText(_translate("SettingDialog", "Reset", None))

        self.ImageLoadPushButton.clicked.connect(self.imagefileLoad)

    def pixelSelect(self, event):
        position = QtCore.QPoint(event.pos().x(), event.pos().y())
        print "x={0} y={1}".format(position.x(), position.y())

    def imagefileLoad(self):
        self.local_image = QtGui.QImage(self.lineEdit.text())
        self.pixMapItem = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(self.local_image), None, self.local_scene)
        self.pixMapItem.mousePressEvent = self.pixelSelect

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = SettingFromImageDialog()
    sys.exit(app.exec_())
