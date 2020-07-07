from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox

from create_link import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(190, 200, 421, 41))
        self.textEdit.setObjectName("textEdit")
        self.search_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.search_pushButton.setGeometry(QtCore.QRect(310, 290, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.search_pushButton.setFont(font)
        self.search_pushButton.setObjectName("search_pushButton")
        self.create_link_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.create_link_pushButton.setGeometry(QtCore.QRect(310, 360, 171, 41))
        self.create_link_pushButton.setObjectName("create_link_pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 90, 241, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.manage_link_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.manage_link_pushButton.setGeometry(QtCore.QRect(310, 430, 171, 41))
        self.manage_link_pushButton.setObjectName("manage_link_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        qcb_nm = QComboBox(self)
        qcb_nm.setGeometry(QtCore.QRect(190, 241, 421, 30))
        self.qcb_nm = qcb_nm


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_pushButton.setText(_translate("MainWindow", "查询表关系"))
        self.create_link_pushButton.setText(_translate("MainWindow", "新建表关系"))
        self.label.setText(_translate("MainWindow", "表关系管理系统"))
        self.manage_link_pushButton.setText(_translate("MainWindow", "管理表关系"))



