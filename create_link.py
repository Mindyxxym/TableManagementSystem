# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_link.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import (QApplication,QMainWindow, QTextEdit,QDesktopWidget,QProgressBar,
    QAction, QPushButton,QToolTip,QFileDialog,QMessageBox,QLabel,QLabel,
    QLineEdit)



class Ui_Form2(object):
    _signal = QtCore.pyqtSignal(str)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(609, 506)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 60, 71, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 130, 87, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(230, 70, 271, 31))
        self.textEdit.setObjectName("textEdit") #name edit
        self.textEdit.setText('dm.')
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 440, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2") #OK键
        #self.pushButton_2.clicked.connect(lambda :self.create_ok(MyWindow()))
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(230, 140, 271, 161))
        self.listWidget.setObjectName("listWidget")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 370, 91, 28))
        self.pushButton.setObjectName("pushButton") #add按钮

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 370, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3") #del按钮
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(230, 310, 271, 31))
        self.textEdit_2.setObjectName("textEdit_2") #relation edit

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Name："))
        self.label_2.setText(_translate("Form", "Relations:"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "OK"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)

        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Form", "add"))
        self.pushButton_3.setText(_translate("Form", "del"))











