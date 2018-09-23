# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'naming.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 363)
        MainWindow.setStyleSheet("background-color: rgb(90, 102, 107)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout"              )
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("QLabel {\n"
"    display: inline-block;\n"  
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding: 10px 14px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"  \n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 7, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setStyleSheet("QRadioButton {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding: 5px 0px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #f0f0f0;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 3, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setStyleSheet("QRadioButton {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding: 5px 0px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #f0f0f0;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 1, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setStyleSheet("QCheckBox {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding: 10px 10px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #f0f0f0;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 5, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding:12px 20px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #fdffeb;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
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
"\n"
"   \n"
"\n"
"    \n"
"\n"
"    color: #fdffeb;\n"
"    text-decoration: none;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setStyleSheet("QRadioButton {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding: 5px 0px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #f0f0f0;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 2, 0, 1, 1)
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setStyleSheet("QRadioButton {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding: 5px 0px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #f0f0f0;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout.addWidget(self.radioButton_7, 4, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout, 0, 3, 3, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding:12px 20px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #fdffeb;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setStyleSheet("QRadioButton {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding: 5px 0px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #f0f0f0;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_2.addWidget(self.radioButton_4, 1, 0, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setStyleSheet("QRadioButton {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding: 5px 0px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #f0f0f0;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_2.addWidget(self.radioButton_5, 2, 0, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setStyleSheet("QRadioButton {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding: 5px 0px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #f0f0f0;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout_2.addWidget(self.radioButton_6, 3, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_2, 0, 2, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding:12px 20px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #fdffeb;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_10.addWidget(self.lineEdit_4, 0, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_10, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setStyleSheet("QLineEdit {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding:12px 0px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #fdffeb;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_7.addWidget(self.lineEdit_5, 0, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setStyleSheet("QLineEdit {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding:12px 0px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #fdffeb;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_7.addWidget(self.lineEdit_6, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setStyleSheet("QPushButton  {\n"
"    \n"
"    \n"
"    display: inline-block;\n"
"    text-align: center;\n"
"    vertical-align: middle;\n"
"    padding:12px 27px;\n"
"    border: 0px solid #a12727;\n"
"    border-radius: 19px;\n"
"    background: #ff4a4a;\n"
"    \n"
"\n"
"   \n"
"\n"
"    \n"
"\n"
"    color: #fdffeb;\n"
"    text-decoration: none;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_10.addWidget(self.pushButton_4, 0, 2, 0, 1)

        self.gridLayout_4.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("QLabel {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding: 0px 0px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #f0f0f0;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setStyleSheet("QPushButton  {\n"
"    \n"
"    \n"
"    display: inline-block;\n"
"    text-align: center;\n"
"    vertical-align: middle;\n"
"    padding:20px 20px;\n"
"    border: 0px solid #a12727;\n"
"    border-radius: 20px;\n"
"    background: #ff4a4a;\n"
"    \n"
"\n"
"   \n"
"\n"
"    \n"
"\n"
"    color: #fdffeb;\n"
"    text-decoration: none;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_8.addWidget(self.pushButton_6, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("QLabel {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding: 0px 0px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #f0f0f0;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 2, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 1, 1, 2, 2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
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
"    color: #fdffeb;\n"
"    text-decoration: none;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 4, 1, 1, 1)
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
"\n"
"   \n"
"\n"
"    \n"
"\n"
"    color: #fdffeb;\n"
"    text-decoration: none;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 3, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding:12px 20px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #fdffeb;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 4, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding:12px 20px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #fdffeb;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 3, 0, 1, 1)
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
"\n"
"    \n"
"\n"
"    color: #fdffeb;\n"
"    text-decoration: none;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("QLabel {\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"\n"
"    vertical-align: middle;\n"
"    padding: 0px 10px;\n"
"    border: 0px solid #b3b3b3;\n"
"    border-radius: 10px;\n"
"    background: #f0f0f0;\n"
"\n"
"\n"
"\n"
"    color: #111111;\n"
"    text-decoration: none;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 23))
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
        self.label.setText(_translate("MainWindow", "Powered By Subscene "))
        self.radioButton_3.setText(_translate("MainWindow", "WEB"))
        self.radioButton.setText(_translate("MainWindow", "Anime"))
        self.checkBox.setText(_translate("MainWindow", "hearing impaired"))
        self.pushButton.setText(_translate("MainWindow", "Download Subtitles"))
        self.radioButton_2.setText(_translate("MainWindow", "Blu-Ray"))
        self.radioButton_7.setText(_translate("MainWindow", "HDTV"))
        self.radioButton_4.setText(_translate("MainWindow", "01,02,03"))
        self.radioButton_5.setText(_translate("MainWindow", "01x01"))
        self.radioButton_6.setText(_translate("MainWindow", "S01E01"))
        self.pushButton_4.setText(_translate("MainWindow", "Tag Example"))
        self.label_2.setText(_translate("MainWindow", "Example"))
        self.pushButton_6.setText(_translate("MainWindow", "Preview and  Rename"))
        self.label_4.setText(_translate("MainWindow", "             Version 1.0.0"))
        self.pushButton_5.setText(_translate("MainWindow", "Catch by  ID"))
        self.pushButton_3.setText(_translate("MainWindow", "Catch TV Name"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse Folder"))
        self.label_3.setText(_translate("MainWindow", "Dedicate to you by \nKickass Torrent katcr.co")) 

