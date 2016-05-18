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

class ProcessingWidget(QtGui.QWidget):
    def __init__(self):
        super(ProcessingWidget, self).__init__()

        #
        self.setupUi(self)

    def setupUi(self, Widget):
        Widget.setObjectName(_fromUtf8("Widget"))
        Widget.resize(344, 103)
        self.progressBar = QtGui.QProgressBar(Widget)
        self.progressBar.setGeometry(QtCore.QRect(40, 40, 271, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Widget", "Processing", None))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = ProcessingWidget()
    ex.show()
    sys.exit(app.exec_())
    
