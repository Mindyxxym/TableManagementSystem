
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage_link.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(613, 506)
        self.move_Button = QtWidgets.QPushButton(Form)
        self.move_Button.setGeometry(QtCore.QRect(450, 170, 101, 31))
        self.move_Button.setObjectName("move_Button")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(40, 360, 341, 31))
        self.textEdit.setObjectName("textEdit")
        self.add_Button = QtWidgets.QPushButton(Form)
        self.add_Button.setGeometry(QtCore.QRect(450, 360, 101, 31))
        self.add_Button.setObjectName("add_Button")
        self.m_ok_Button = QtWidgets.QPushButton(Form)
        self.m_ok_Button.setGeometry(QtCore.QRect(270, 440, 101, 31))
        self.m_ok_Button.setObjectName("m_ok_Button")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(40, 40, 341, 291))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.move_Button.setText(_translate("Form", "move"))
        self.add_Button.setText(_translate("Form", "add"))
        self.m_ok_Button.setText(_translate("Form", "OK"))
