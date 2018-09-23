# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rename.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 602)
        MainWindow.setStyleSheet("background-color:rgb(100, 100, 100)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setStyleSheet("QTreeView {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding: 0px 0px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #ffffff;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.treeView.setObjectName("treeView")
        self.gridLayout.addWidget(self.treeView, 0, 0, 1, 1)
        self.treeView_2 = QtWidgets.QTreeView(self.centralwidget)
        self.treeView_2.setStyleSheet("QTreeView {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding: 0px 0px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #ffffff;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.treeView_2.setObjectName("treeView_2")
        self.gridLayout.addWidget(self.treeView_2, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet("QPushButton  {\n"
"    \n"
"    \n"
"    display: inline-block;\n"
"    text-align: center;\n"
"    vertical-align: middle;\n"
"    padding:12px 20px;\n"
"    border: 0px solid #a12727;\n"
"    border-radius: 19px;\n"
"    background: #ff4a4a;\n"
"    \n"
"    image: url(up.png);\n"
"   \n"
"\n"
"    \n"
"\n"
"    color: #ffffff;\n"
"    text-decoration: none;\n"
"}")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_5.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setStyleSheet("QPushButton  {\n"
"    \n"
"    \n"
"    display: inline-block;\n"
"    text-align: center;\n"
"    vertical-align: middle;\n"
"    padding:12px 20px;\n"
"    border: 0px solid #a12727;\n"
"    border-radius: 19px;\n"
"    background: #ff4a4a;\n"
"    \n"
"\n"
"   image: url(down.png);\n"
"\n"
"    \n"
"\n"
"    color: #ffffff;\n"
"    text-decoration: none;\n"
"}")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_5.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_5.addLayout(self.verticalLayout_2, 4, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setStyleSheet("QPushButton  {\n"
"    \n"
"    \n"
"    display: inline-block;\n"
"    text-align: center;\n"
"    vertical-align: middle;\n"
"    padding:12px 20px;\n"
"    border: 0px solid #a12727;\n"
"    border-radius: 19px;\n"
"    background: #ff4a4a;\n"
"    \n"
"    image: url(trash.png);\n"
"\n"
"   \n"
"\n"
"    \n"
"\n"
"    color: #ffffff;\n"
"    text-decoration: none;\n"
"}")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_5.addWidget(self.pushButton_7, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_2.addLayout(self.verticalLayout_4, 5, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_2.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("QPushButton  {\n"
"    \n"
"    \n"
"    display: inline-block;\n"
"    text-align: center;\n"
"    vertical-align: middle;\n"
"    padding:12px 20px;\n"
"    border: 0px solid #a12727;\n"
"    border-radius: 19px;\n"
"    background: #ff4a4a;\n"
"    \n"
"    image: url(down.png);\n"
"\n"
"   \n"
"\n"
"    \n"
"\n"
"    color: #ffffff;\n"
"    text-decoration: none;\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("QPushButton  {\n"
"    \n"
"    \n"
"    display: inline-block;\n"
"    text-align: center;\n"
"    vertical-align: middle;\n"
"    padding:12px 20px;\n"
"    border: 0px solid #a12727;\n"
"    border-radius: 19px;\n"
"    background: #ff4a4a;\n"
"    \n"
"\n"
"   \n"
"    image: url(up.png);\n"
"\n"
"    \n"
"\n"
"    color: #ffffff;\n"
"    text-decoration: none;\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_6.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setStyleSheet("QPushButton  {\n"
"    \n"
"    \n"
"    display: inline-block;\n"
"    text-align: center;\n"
"    vertical-align: middle;\n"
"    padding:12px 20px;\n"
"    border: 0px solid #a12727;\n"
"    border-radius: 19px;\n"
"    background: #ff4a4a;\n"
"    \n"
"    image: url(trash.png);\n"
"   \n"
"\n"
"    \n"
"\n"
"    color: #ffffff;\n"
"    text-decoration: none;\n"
"}")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_6.addWidget(self.pushButton_6, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_6, 3, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setStyleSheet("QPushButton  {\n"
"    \n"
"    \n"
"    display: inline-block;\n"
"    text-align: center;\n"
"    vertical-align: middle;\n"
"    padding:12px 20px;\n"
"    border: 0px solid #a12727;\n"
"    border-radius: 19px;\n"
"    background: #ff4a4a;\n"
"    \n"
"\n"
"   \n"
"\n"
"    \n"
"\n"
"    color: #ffffff;\n"
"    text-decoration: none;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.pushButton_5, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "Rename"))
