# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PaintOnAPanel.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(784, 427)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(784, 427))
        Dialog.setMaximumSize(QtCore.QSize(784, 427))
        self.DrawingFrame = QtGui.QStackedWidget(Dialog)
        self.DrawingFrame.setGeometry(QtCore.QRect(120, 10, 651, 411))
        self.DrawingFrame.setFrameShape(QtGui.QFrame.Box)
        self.DrawingFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.DrawingFrame.setObjectName(_fromUtf8("DrawingFrame"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.DrawingFrame.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.DrawingFrame.addWidget(self.page_2)
        self.BrushErase_Button = QtGui.QPushButton(Dialog)
        self.BrushErase_Button.setGeometry(QtCore.QRect(10, 10, 101, 23))
        self.BrushErase_Button.setObjectName(_fromUtf8("BrushErase_Button"))
        self.ChangeColour_Button = QtGui.QPushButton(Dialog)
        self.ChangeColour_Button.setGeometry(QtCore.QRect(10, 40, 101, 23))
        self.ChangeColour_Button.setObjectName(_fromUtf8("ChangeColour_Button"))
        self.Thickness_Spinner = QtGui.QSpinBox(Dialog)
        self.Thickness_Spinner.setGeometry(QtCore.QRect(20, 80, 81, 22))
        self.Thickness_Spinner.setProperty("value", 10)
        self.Thickness_Spinner.setObjectName(_fromUtf8("Thickness_Spinner"))
        self.Clear_Button = QtGui.QPushButton(Dialog)
        self.Clear_Button.setGeometry(QtCore.QRect(10, 400, 101, 23))
        self.Clear_Button.setObjectName(_fromUtf8("Clear_Button"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.BrushErase_Button.setText(_translate("Dialog", "Brush/Erase", None))
        self.ChangeColour_Button.setText(_translate("Dialog", "Change Colour", None))
        self.Clear_Button.setText(_translate("Dialog", "Clear", None))
