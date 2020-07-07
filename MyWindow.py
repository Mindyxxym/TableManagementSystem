import json
import os
from functools import reduce

from PyQt5.QtWidgets import QMainWindow
from pyecharts.charts import Graph

from Form3 import Ui_Form3
from mainWindow import Ui_MainWindow
from pyecharts import options as opts
from pyecharts.charts import Graph, Page,Tree
from create_link import *
from manage_link import Ui_Form

from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

sys.setrecursionlimit(9000000)

class MyWindow(QMainWindow, Ui_MainWindow):
    _signal_1 = QtCore.pyqtSignal(list,list)
    _signal_0 = QtCore.pyqtSignal(list,list,str)
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        #self.form2 = Form2()
        self.form3 = Form3()
       # self.w_create = QtWidgets.QWidget()
        #self.form2(self.w_create)
        #self.nodes = [{'name': 'dm.a', 'symbolSize': 20}, {'name': 'dm.b', 'symbolSize': 20},{'name': 'dw.c', 'symbolSize': 20}]
        #self.links = [{'source': 'dm.a', 'target': 'dm.b'},{'source':'dm.b','target':'dw.c'}]
        self.category = [{'name':'dm','symbol_size':20},{'name':'dw','symbol_size':15}]
        with open('./nodes.json', 'r') as f:
            self.nodes = json.load(f)
        with open('./links.json', 'r') as f:
            self.links = json.load(f)
        #self.qcb_nm.currentIndexChanged[int].connect(lambda:self.nm_changed())
        self.qcb_nm.hide()
        self.create_link_pushButton.clicked.connect(lambda: self.open_form2())
        #self._signal_1.connect(self.form2.get_data)
        #self._signal_0.connect(self.form1.get_data2)
        self.search_pushButton.clicked.connect(lambda :self.search())
        self.manage_link_pushButton.clicked.connect(lambda :self.open_form1())
        self.textEdit.textChanged.connect(lambda:self.nm_changed(self.textEdit.toPlainText()))
        self.qcb_nm.activated.connect(lambda :self.qcb_get())
        #self.qcb_nm.activated.connect(lambda :self.showPopup())


    def open_form1(self):
        self.form1 = Form1()
        self._signal_0.connect(self.form1.get_data2)
        t_name = self.textEdit.toPlainText()
        if not self.get_index(t_name)==-1:
            self.form1.show()
            self._signal_0.emit(self.nodes,self.links,t_name)
            self.form1._signal2.connect(self.getData_F2)
            self.form1.setWindowTitle(t_name)
        else:
            QMessageBox.warning(self, 'Notice', "该表不存在！")


    def nm_changed(self,text):
        if self.textEdit.hasFocus() == True:
            self.qcb_nm.show()
            self.qcb_nm.clear()
            a = self.qcb_nm.currentIndex()
            for i in self.nodes:
                if text in i['name']:
                   self.qcb_nm.addItem(i['name'].replace('\n\n','  '))



    def qcb_get(self):
        if self.qcb_nm.hasFocus() == True:
            name = self.qcb_nm.currentText().split('  ',1)[0]
            self.textEdit.setText(name)
            self.qcb_nm.hide()

    def open_form2(self):
        self.form2 = Form2()
        self._signal_1.connect(self.form2.get_data)
        self.form2.show()
        self._signal_1.emit(self.nodes, self.links)
        self.form2._signal.connect(self.getData_F2)

    def getData_F2(self,nodes,links):
        self.nodes = nodes
        self.links = links

    def input_node(self,name):
        new_node = {}

        if name[:2]=='dm':
            new_node['category'] = 0
            new_node['name'] = name
        else:
            new_node['category'] = 1
            new_node['name'] =self.get_dw_name(name)
        new_node['value'] = 0
        new_node['symbolSize'] = 20

        '''new_node['category'] = k[:2]'''

        return new_node

    def input_link(self,source, target):
        if target[:2] == 'dw':
            target = self.get_dw_name(target)
        new_link = {}
        new_link['source'] = source
        new_link['target'] = target
        return new_link

    def is_new_node(self,name,nodes):
        for i in nodes:
            if name == i['name']:
                return False
        return True

    def get_index(self,t_name):
        k=0
        for i in self.nodes:
            if i['name'].split('\n\n',1)[0] == t_name.split('\n\n',1)[0]:
                return k
            k += 1
        return -1
    '''
    def get_index(self,t_name):
        k = 0
        if t_name[:2] == 'dm':
            for i in self.nodes:
                if i['name'] == t_name:
                    return k
                k += 1
            return -1
        else:

            for i in self.nodes:
                if i['name'].split('\n\n',1)[0] == t_name.split('\n\n',1)[0]:
                    return k
                k += 1
            return -1
    '''
    '''
    def search_link_all(self,t_name,links):
        for i in links:
            if i['source'] == t_name:
                t_link = self.input_link(t_name, i['target'])
                self.new_link.append(t_link)
                index = self.get_index(i['target'])
                self.new_nodes.append(self.nodes[index])
                if i['target'][:3] == "dm.":
                    self.search_link_all(i['target'], links)
        return 1
    '''

    class Node:

        def add_child(self,child):
            self.children.append(child)
            self.info ['children']=self.children

        def __init__(self, name):
            self.name = name
            self.children =[]
            self.info={}
            self.info['name'] = name


    def search_link_all(self,t_name,new_links=[],new_nodes=[],node_dic={}):
        if self.is_new_node(t_name,new_nodes):
            index = self.get_index(t_name)

            new_nodes.append(self.nodes[index])
            links =[]
            if self.tree_flag==1 and t_name not in node_dic.keys():
                node_dic[t_name] =self.Node(t_name)
            if t_name[:3] == "dm_":

                for i in self.links:
                    if i['source'] == t_name:
                        t_link = self.input_link(t_name, i['target'])
                        new_links.append(t_link)
                        links.append(i['target'])
                        if self.tree_flag==1:
                            node_dic[i['target']] = self.Node(i['target'])
                            node_dic[t_name].add_child(node_dic[i['target']].info)
                for i in links:
                    self.search_link_all(i,new_links,new_nodes,node_dic)
        return new_links,new_nodes,node_dic




    def get_dw_name(self,t_name):
        index = self.get_index(t_name)
        if index ==-1:
            return t_name
        return self.nodes[index]['name']


    def search(self):
        t_name = self.textEdit.toPlainText()
        #if t_name[:2] == 'dw':
        t_name = self.get_dw_name(t_name)
        if not self.is_new_node(t_name,self.nodes) or t_name in ('all','lgs','wms'):

            self.new_nodes = []
            self.new_link = []
            self.tree_flag=-1
            if t_name == 'all':
                self.new_nodes = self.nodes
                self.new_link = self.links
                self.tree_flag=0
            elif t_name == 'lgs' or t_name == 'wms':
                self.tree_flag = 0
                for i in self.nodes:
                    wms_flag = t_name == 'wms' and "warehouse" in i['name']
                    if t_name in i['name'] or wms_flag:
                        res = self.search_link_all(i['name'], [], [],[])
                        #for j,k in res[1],res[0]:
                        #    if j not in self.new_nodes:
                        #        self.new_nodes.append(j)
                        #    if k not in self.new_link
                        self.new_nodes.extend(res[1])
                        self.new_link.extend(res[0])
                self.new_link= reduce(lambda x,y:x if y in x else x + [y], [[],] + self.new_link)
                self.new_nodes=reduce(lambda x,y:x if y in x else x + [y], [[],] + self.new_nodes)

            else:
                #index = self.get_index(t_name)
                #self.new_nodes.append(self.nodes[index])
                #self.search_link_all(t_name,self.links)
                self.tree_flag = 1

                res = self.search_link_all(t_name,[],[],{})
                self.new_nodes = res[1]
                self.new_link = res[0]
                data = [res[2][t_name].info]




            if self.tree_flag ==1:
                 tree = Tree()
                 tree.width = '1800px'
                 tree.height = '950px'
                 tree.add(
                     "",
                     data,
                     pos_top="middle",
                     pos_left="center",
                     is_roam =True,
                     label_opts=opts.LabelOpts(
                         position="top",
                         font_size = 12,
                         vertical_align='middle'
                        ),
                     leaves_label_opts=opts.LabelOpts(
                         position="right",
                         font_size=12,
                         vertical_align='middle',
                         color = "#6B238E"
                     )
                     #,pos_top='middle',pos_left='center'
                  )
                 tree.set_global_opts(title_opts=opts.TitleOpts(title=t_name.split('\n\n', 1)[0] + "依赖关系"))
                 tree.render()


            elif self.tree_flag == 0:
                graph = Graph()
                graph.width = '1800px'
                graph.height = '950px'
                # graph.in

                graph.add(
                    "",
                    self.new_nodes,
                    self.new_link,
                    self.category,
                    repulsion=7000,
                    # layout = "circular",
                    is_focusnode=True,
                    is_draggable=True,
                    edge_label=True,
                    edge_length=60,
                    edge_symbol=['line', 'arrow'],
                    label_opts=opts.LabelOpts(is_show=True, position="top", ),
                    linestyle_opts=opts.LineStyleOpts(is_show=True, color="target", curve=0.3, opacity=0.7, )
                )
                graph.set_global_opts(title_opts=opts.TitleOpts(title=t_name + "依赖关系"))
                graph.render()
                #print(self.new_nodes,self.new_link)
                #nodes_j = json.dumps(new_nodes)
                #links_j = json.dumps(new_links)




            #print(nodes_j,links_j)

            #self.setCentralWidget(self.form2)
            #self.form2.show()
            '''
            self.form2.show()
            self.form2.view = QWebEngineView(self.form2)
            web = QUrl("C:/Users/USER/PycharmProjects/untitled1/render.html")
            self.form2.view.load(web)
            self.form2.setCentralWidget(self.form2.view)
            self.form2.view.show()
            '''

            self.form3.setWindowTitle("Relations of "+t_name.split('\n\n', 1)[0])
            self.form3.setGeometry(60, 45, 1800, 950)

            self.form3.view = QWebEngineView(self.form3)
            #web = QUrl("C:/Users/USER/PycharmProjects/untitled1/render.html")
            web = QUrl(QFileInfo("./render.html").absoluteFilePath())
            self.form3.view.load(web)

            self.form3.setCentralWidget(self.form3.view)
            #self.form2.setGeometry(5,30,1355,730)
            self.form3.show()
            #self.form3.view.resize(1800, 950)
            #self.form3.view.showMaximized()
            #self.form3.view.show()



        else:

            QMessageBox.warning(self, 'Notice', "该表不存在！")


class Form2(QMainWindow,Ui_Form2):
    _signal = QtCore.pyqtSignal(list,list)
    def __init__(self):
        super(Form2, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.pushButton.clicked.connect(lambda: self.addLink(self.textEdit_2.toPlainText()))
        self.pushButton_3.clicked.connect(lambda:self.delLink())
        self.pushButton_2.clicked.connect(lambda: self.create_ok())
        self.nodes= []
        self.links = []
        self.listWidget.clear()
        self.textEdit.clear()
        self.textEdit_2.clear()


    def get_data(self,nodes,links):
        self.nodes = nodes
        self.links = links





    def create_ok(self):

        loader = MyWindow()


        t_name = self.textEdit.toPlainText()
        link_num = self.listWidget.count()


        if bool(t_name) and t_name[:3] == 'dm_' and link_num !=0:

            if loader.is_new_node(t_name,self.nodes):
                res = loader.input_node(t_name)
                self.nodes.append(res)
                link_list = []
                for i in range (link_num):
                    link_list.append(self.listWidget.item(i).text())
                for i in link_list:
                    #if loader.is_new_node(i,self.nodes):
                    if loader.get_index(i) == -1:   #新结点
                        tmp = loader.input_node(i)
                        self.nodes.append(tmp)
                    t_link = loader.input_link(t_name,i)
                    #这个节点的value++
                    self.links.append(t_link)
                    index = loader.get_index(i)
                    self.nodes[index]['value'] += 1
                    self.nodes[index]['symbolSize'] += 4
                #在这里加json的存储

                self._signal.emit(self.nodes,self.links)
                self.textEdit_2.setText('')
                self.textEdit.setText('')
                self.listWidget.clear()
                QMessageBox.information(self,'Notice','创建成功')
                save_node = json.dumps(self.nodes)
                save_link = json.dumps(self.links)
                f1 = open('./nodes.json','w')
                f2 = open('./links.json', 'w')
                f1.write(save_node)
                f2.write(save_link)
                f1.close()
                f2.close()

                self.close()
            else:
                QMessageBox.warning(self.listWidget, 'Notice', "该表已存在！")
        else:
            if link_num ==0:
                QMessageBox.warning(self.listWidget, 'Notice', "关系不得为空！")
            else:
                QMessageBox.warning(self.listWidget, 'Notice', "表名不规范！")

        del loader

    def addLink(self,add_name):
        if  bool(add_name) and (add_name[:3] == 'dm_' or add_name[:3] == 'dw_'):
            if len(self.listWidget.findItems(add_name,QtCore.Qt.MatchExactly) ) != 0 :
                QMessageBox.warning(self.listWidget, 'Notice', "请勿重复输入！")
            else:
                self.listWidget.addItem(add_name)
                self.textEdit_2.setText('')
        else:
            QMessageBox.warning(self.listWidget,'Notice',"表名不规范！")

    def delLink(self):
        del_item = self.listWidget.currentItem()
        self.listWidget.takeItem(self.listWidget.row(del_item))

class Form3(QMainWindow,Ui_Form3):
    def __init__(self):
        super(Form3, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.new_nodes = []
        self.new_link = []



class Form1(QMainWindow,Ui_Form):
    _signal2 = QtCore.pyqtSignal(list, list)
    def __init__(self):
        super(Form1, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.add_Button.clicked.connect(lambda :self.add_link())
        self.move_Button.clicked.connect(lambda :self.delLink())
        self.m_ok_Button.clicked.connect(lambda :self.m_ok())




    def get_data2(self,nodes, links,t_name):
        self.nodes = nodes
        self.links = links
        loader = MyWindow()
        self.t_name = loader.get_dw_name(t_name)


        if t_name[:2]=='dw':
            self.move_Button.hide()
            self.add_Button.hide()
            self.listWidget.hide()
            self.index = loader.get_index(t_name)
            self.textEdit.setText(self.t_name.split('\n\n',1)[-1])
        else:
            for i in links:
                if self.t_name == i['source']:
                    #if i['target'][:2] == 'dw':
                    name = i['target'].split('\n\n',1)[0]
                    self.listWidget.addItem(name)
                    #else:
                     #   self.listWidget.addItem(i['target'])


    def add_link(self):
        add_name = self.textEdit.toPlainText()
        if bool(add_name) and (add_name[:3] == 'dm_' or add_name[:3] == 'dw_'):
            if len(self.listWidget.findItems(add_name, QtCore.Qt.MatchExactly)) != 0:
                QMessageBox.warning(self.listWidget, 'Notice', "请勿重复输入！")
            else:
                self.listWidget.addItem(add_name)
                '''
                检测add_name是不是新结点，是的话加入nodes
                添加t_name和add_name的关系到links
                '''
                loader = MyWindow()
                if loader.get_index(add_name)==-1:
                    res = loader.input_node(add_name)
                    self.nodes.append(res)
                res = loader.input_link(self.t_name,add_name)
                self.links.append(res)
                index = loader.get_index(add_name)
                self.nodes[index]['value'] += 1
                self.nodes[index]['symbolSize'] += 4

                del loader
                self.textEdit.clear()
        else:
            QMessageBox.warning(self.listWidget, 'Notice', "表名不规范！")

    def delLink(self):
        del_item = self.listWidget.currentItem()
        self.listWidget.takeItem(self.listWidget.row(del_item))
        '''
        删除t_name 到 del_name的关系（是否要检测）
        如果这是del_name的最后一个关系，将del_name移出nodes
        '''
        del_name = del_item.text()
        loader = MyWindow()
        res = loader.input_link(self.t_name,del_name)
        self.links.remove(res)
        if del_name[:2] == 'dw':
            del_name = loader.get_dw_name(del_name)

        is_only = self.is_only_node(del_name,self.links)
        if is_only == True:
            res = loader.get_index(del_name)
            del self.nodes[res]
        else:
            index = loader.get_index(del_name)
            self.nodes[index]['value'] -= 1
            self.nodes[index]['symbolSize'] -= 4
        del loader

    def is_only_node(self,node,links):
        for i in links:
            if i['source'] == node or i['target'] == node:
                return False
        return True


    def m_ok(self):
        '''
            检查是否都删了，list为0，是的话询问是否删表
            传送nodes回去
        '''

        if self.t_name[:2] == 'dw':
            t_name = self.t_name.split('\n\n', 1)[0]
            txt = self.textEdit.toPlainText()
            name = t_name +'\n\n'+txt
            #dw_name = self.nodes[self.index]['name']
            for i in self.links :
                if i['target'] == self.t_name:
                    i['target'] = name
            self.nodes[self.index]['name'] = name
        else:

            if self.listWidget.count()==0:
                reply = QMessageBox.question(self,'Message','检测该表关系为空，是否删除该表？',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes )
                if reply == QMessageBox.Yes:
                    loader = MyWindow()
                    is_only = self.is_only_node(self.t_name, self.links)
                    if is_only == True:
                        res = loader.get_index(self.t_name)
                        del self.nodes[res]

        self._signal2.emit(self.nodes, self.links)
        QMessageBox.information(self, 'Notice', '修改成功')
        save_node = json.dumps(self.nodes)
        save_link = json.dumps(self.links)
        f1 = open('./nodes.json', 'w')
        f2 = open('./links.json', 'w')
        f1.write(save_node)
        f2.write(save_link)
        f1.close()
        f2.close()
        self.listWidget.clear()
        self.textEdit.clear()
        self.close()


