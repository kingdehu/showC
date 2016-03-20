# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindows.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_mainWindows(object):
    def setupUi(self, mainWindows):
        mainWindows.setObjectName(_fromUtf8("mainWindows"))
        mainWindows.resize(800, 600)
        self.DrawFrame = QtGui.QStackedWidget(mainWindows)
        self.DrawFrame.setGeometry(QtCore.QRect(170, 100, 400, 400))
        self.DrawFrame.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.DrawFrame.setObjectName(_fromUtf8("DrawFrame"))
        self.DrawFramePage1 = QtGui.QWidget()
        self.DrawFramePage1.setObjectName(_fromUtf8("DrawFramePage1"))
        self.DrawFrame.addWidget(self.DrawFramePage1)
        self.pd_U = QtGui.QPushButton(mainWindows)
        self.pd_U.setGeometry(QtCore.QRect(580, 140, 111, 51))
        self.pd_U.setObjectName(_fromUtf8("pd_U"))
        self.pb_UR = QtGui.QPushButton(mainWindows)
        self.pb_UR.setGeometry(QtCore.QRect(580, 220, 111, 51))
        self.pb_UR.setObjectName(_fromUtf8("pb_UR"))

        self.retranslateUi(mainWindows)
        QtCore.QMetaObject.connectSlotsByName(mainWindows)

    def retranslateUi(self, mainWindows):
        mainWindows.setWindowTitle(_translate("mainWindows", "Dialog", None))
        self.pd_U.setText(_translate("mainWindows", "0", None))
        self.pb_UR.setText(_translate("mainWindows", "45", None))

