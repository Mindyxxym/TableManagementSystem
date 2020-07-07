import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from MyWindow import MyWindow
from mainWindow import *
from create_link import *
from manage_link import *
import os
import json
from pyecharts import options as opts
from pyecharts.charts import Graph, Page


            





if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    #w_manage = QtWidgets.QWidget()
    #w_create = QtWidgets.QWidget()
    #b = Ui_Form()
    #b.setupUi(w_manage)
    #c = Ui_Form2()
    #c.setupUi(w_create)


    myWin.show()
    #myWin.search_pushButton.clicked.connect(lambda :myWin.search(nodes,links))
    #myWin.create_link_pushButton.clicked.connect(w_create.show)
   # myWin.manage_link_pushButton.clicked.connect(w_manage.show)



    sys.exit(app.exec_())





