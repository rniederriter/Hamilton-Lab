# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'repetition.ui'
#
# Created: Thu Jul 14 22:10:29 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 263)
        font = QtGui.QFont()
        font.setPointSize(7)
        Dialog.setFont(font)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 140, 61, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.RepNum = QtGui.QSpinBox(Dialog)
        self.RepNum.setGeometry(QtCore.QRect(110, 110, 46, 22))
        self.RepNum.setObjectName(_fromUtf8("RepNum"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 90, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "Infinite", None))
        self.label.setText(_translate("Dialog", "Repetition", None))

