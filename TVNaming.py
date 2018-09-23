from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtGui import QKeyEvent,QFocusEvent,QPixmap
from PyQt5.QtCore import QEvent,QModelIndex
import time
import threading
from splash import Ui_MainWindow as sp
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox , QDialogButtonBox,QFileDialog
import sys
import sqlite3
from namingU import Ui_MainWindow as mainos
from rename import Ui_MainWindow as renameod
import platform
import urllib3
http = urllib3.PoolManager()
import pytvmaze
import re
import webbrowser
import os
import inflect
import subscene
from os.path import expanduser
import requests
import zipfile

urllib3.disable_warnings()
p = inflect.engine()
dir = []
sources = []
output = []
errors = [0]
prog = [0]
extentions = ['.aqt', '.cvd', '.dks', '.jss', '.sub', '.ttxt', '.mpl', '.txt', '.sub', '.pjs', '.psb', '.rt',
                      '.smi', '.ssf', '.srt', '.ssa', '.sub', '.svcd', '.usf', '.sub,', '.txt', '.ass']
class extratror(object):
    filessub = []
    idx = []
    custemdict = {}
    def deepmoed(self,tt,yy):
        errors.insert(0,2)
        errors.insert(1,yy)

    def extractor(self,fir,all,tt):
        try:
            self.zip_ref = zipfile.ZipFile(all, 'r')
        except:
            self.deepmoed(tt,fir)
        else:
            self.zip_ref.extractall(self.downfolder)
            self.zip_ref.close()





    def __init__(self,language,tt):
        self.downfolder = str(dir[0]) + '/' + 'dummytemp'
        for self.file in os.listdir(self.downfolder):
            if self.file.endswith('.zip'):
                self.fuldir = self.downfolder + '/' + self.file
                self.extractor(all=self.fuldir,fir=self.file,tt=tt)

        for self.subtitle in  os.listdir(self.downfolder):
            for self.extention in extentions:
                if self.subtitle.endswith(self.extention):
                    self.filessub.append(self.subtitle)
                elif self.subtitle.endswith(".idx"):
                    self.idx.append(self.subtitle)
        if len(self.idx) != 0:
            for self.sub in self.filessub:
                for self.idxs in self.idx:
                    if self.sub[:-4] == self.idxs:
                        self.temp = {self.sub:self.idxs}
                        self.custemdict.update(self.temp)

        else:
            for self.names in sources:
                for self.subfileoo in self.filessub:
                    self.one = re.findall(r'\d+', self.names)
                    self.two = re.findall(r'\d+', self.subfileoo)
                    if self.one[1] == self.two[1]:
                        self.out = str(dir[0]) + "/" + self.names[:-4] + '.' + language + self.subfileoo[-4:]
                        self.input = self.downfolder  + '/' + self.subfileoo
                        os.rename(self.input,self.out)
        if len(self.idx) != 0:
            for self.names in sources:
                for self.subfileoo, self.idname in self.custemdict.items():
                    self.one = re.findall(r'\d+', self.names)
                    self.two = re.findall(r'\d+', self.subfileoo)
                    if self.one[1] == self.two[1]:
                        self.out2 = str(dir[0]) + "/" + self.names[:-4] + '.' + language + self.idname[-4:]
                        self.out = str(dir[0]) + "/" + self.names[:-4] + '.' + language + self.subfileoo[-4:]
                        self.input = self.downfolder + '/' + self.subfileoo
                        os.rename(self.input, self.out)
                        os.rename(self.input, self.out2)

        prog.insert(0,100)
        self.filessub.clear()
        self.idx.clear()
        self.custemdict.clear()

        sources.clear()
        output.clear()





class subscenes(object):
    tempdata = {}
    templan = []
    tempfine = []
    downloaded = []
    def deepmoed(self,tt):
        errors.insert(0,3)
    def nosub(self,tt):
        errors.insert(0,2)
        prog.insert(0,100)

    def downloaders(self,some):
        try:
            self.zipfile = http.request('GET', self.subtitle[some].zipped_url,
                                        preload_content=False)
        except:
            self.downloaders(some)
        else:
            self.downfolder = str(dir[0]) + '/' + 'dummytemp' + '/' + str(self.subtitle[some]) + '.zip'
            with open(self.downfolder, 'wb') as self.gb:
                self.gb.write(self.zipfile.read())
            self.gb.close()




    def __init__(self,name,kind,season,hearing,langugage,tt):
        if prog[0] < 5:
            prog.insert(0,5)
        self.u = 0

        self.seasonchars = p.ordinal(season)
        self.seasonnumber =  p.number_to_words(self.seasonchars)
        self.searchname  = name + " - " + self.seasonnumber + " " + "Season"

        try:
            self.film = subscene.search(self.searchname)
            self.subtitle = self.film.subtitles
        except:
            self.deepmoed(tt)
            try:
                self.film = subscene.search(name)
                self.subtitle = self.film.subtitles
            except:
                self.nosub(tt)
            else:
                if prog[0] < 10:
                    prog.insert(0, 10)
                for self.all in self.subtitle:
                    self.tempdict = {self.u: self.all.language}
                    self.tempdata.update(self.tempdict)
                    self.u += 1
        else:
            if prog[0] < 10:
                prog.insert(0,10)
            for self.all in self.subtitle:
                self.tempdict = {self.u:self.all.language}
                self.tempdata.update(self.tempdict)
                self.u += 1
        if prog[0] < 15:
            prog.insert(0, 15)
        for self.id,self.lang in self.tempdata.items():
            if self.lang == langugage:
                self.templan.append(self.id)
        if prog[0] < 20:
            prog.insert(0,20)
        if hearing == True:
            for self.file in self.templan:
                if ("hi" in self.subtitle[int(self.file)].description.lower()) and ("hi removed" not in self.subtitle[int(self.file)].description.lower()):
                    self.tempfine.append(self.file)
        else:
            for self.file in self.templan:
                if ("hi" not in self.subtitle[int(self.file)].description.lower()) or ("hi removed"  in self.subtitle[int(self.file)].description.lower()):
                    self.tempfine.append(self.file)
        if prog[0] < 25:
            prog.insert(0, 25)
        self.templan.clear()
        if kind == "one":
            for self.fine in self.tempfine:
                self.templan.append(self.fine)
        elif kind == "two":
            for self.fine in self.tempfine:
                if "bluray" in str(self.subtitle[self.fine]).lower():
                    self.templan.append(self.fine)

        elif kind == "three":
            for self.fine in self.tempfine:
                if "web" in str(self.subtitle[self.fine]).lower():
                    self.templan.append(self.fine)
        elif kind == "four":
            for self.fine in self.tempfine:
                if "hdtv" in str(self.subtitle[self.fine]).lower():
                    self.templan.append(self.fine)
        else:
            self.nosub(tt)
        if prog[0] < 30:
            prog.insert(0,30)

        self.tempfine.clear()
        if prog[0] < 35:
            self.kilo = 35
        else:
            self.kilo = int(prog[0])
        os.chdir(str(dir[0]))
        try:
            os.makedirs('dummytemp')
        except:
            pass
        else:
            pass
        self.numberoffiles = len(output) + 1

        for self.download in self.templan:
            prog.insert(0,self.kilo)
            if self.subtitle[self.download] not in self.tempfine:
                for self.filereader in range(1,self.numberoffiles):
                    if kind == "one":

                        if "{0:0=2d}".format(self.filereader) not in self.downloaded:
                            self.test = 70 / self.numberoffiles

                            self.kilo = int(self.test) + self.kilo

                            self.downloaders(self.download)
                            self.downloaded.append(self.filereader)
                            self.zipfile.release_conn()
                    elif kind == "two":

                        if len(self.downloaded) == 0:

                            self.zipfile = http.request('GET', self.subtitle[self.download].zipped_url,
                                                        preload_content=False)
                            self.downloaders(self.download)
                            self.kilo = 90
                            self.zipfile.release_conn()
                            self.downloaded.append('done')


                    if kind == "three" or kind == "four":
                        self.gauging = str("{0:0=2d}".format(int(season))) + str("{0:0=2d}".format(int(self.filereader)))
                        if self.gauging not in self.downloaded:

                            if (str("{0:0=2d}".format(int(self.filereader)))  in str(self.subtitle[self.download])) and (str("{0:0=2d}".format(int(season))) in str(self.subtitle[self.download])) == True:
                                self.test = 70 / self.numberoffiles

                                self.kilo = int(self.test) + self.kilo


                                self.downloaders(self.download)

                                self.downloaded.append(self.gauging)
                                self.zipfile.release_conn()
        extratror(langugage,tt)
        self.tempdata.clear()
        self.templan.clear()
        self.tempfine.clear()
        self.downloaded.clear()












class TVMAZE(object):
    def notfoundname(self,yy):
        QMessageBox.about(yy, "error", "We couldn't find Series with that name")
    def notimdb(self,yy):
        QMessageBox.about(yy, "error", "We couldn't find Series with that IMDB code")
    def notmaxe(self,yy):
        QMessageBox.about(yy, "error", "We couldn't find Series with that TvMaz ID")
    def nasty(self,yy):
        QMessageBox.about(yy, "error", "Something nasty happen")
    def __init__(self,name=None,id=None,tt=None):

        if name != "" and name != None:
            try:
                show = tvm.get_show(show_name=name)
            except:
                self.notfoundname(tt)
            else:
                self.sname = show.name
                self.id = show.maze_id
                ApplicationWindow.flashback(tt, name=self.sname, id=self.id)

        elif id != "" and id != None:
            if len(id) == 9:
                try:

                    sshow = tvm.get_show(imdb_id=id)
                except:
                    self.notimdb(tt)
                else:
                    self.mazeid = sshow.maze_id
                    show = tvm.get_show(maze_id=self.mazeid)
                    self.sname = show.name
                    self.id = show.maze_id

                    ApplicationWindow.flashback(tt, name=self.sname, id=self.mazeid)

            else:
                try:
                    show = tvm.get_show(maze_id=id)
                except:
                    self.notmaxe(tt)
                else:


                    self.sname = show.name
                    self.id = show.maze_id
                    ApplicationWindow.flashback(tt, name=self.sname, id=self.id)
        else:
            self.nasty(tt)


class rename(QtWidgets.QMainWindow):
    def warn(self):
        QMessageBox.about(self, "error", "the source file are less than output name!!")
    def warn1(self):
        QMessageBox.about(self, "error", "the source file are more than output name!!")
    def sucess(self):
        QMessageBox.about(self, "Succuss", "Rename was Succussful")
    def renaming(self,u):
        self.sourceid = self.ui.treeView.model().index(self.num, 0)
        self.sourcename = self.ui.treeView.model().data(self.sourceid, QtCore.Qt.DisplayRole)
        self.outid = self.ui.treeView_2.model().index(self.num, 0)
        self.outname = self.ui.treeView_2.model().data(self.outid, QtCore.Qt.DisplayRole)
        self.outputful = self.outname +  self.sourcename[-4:]
        self.sourcefulenth = str(dir[0]) + '/' + self.sourcename
        self.outfulenth = str(dir[0]) + '/' + self.outputful
        os.rename(self.sourcefulenth, self.outfulenth)
    def rename(self):
        self.outlenth = self.ui.treeView_2.model().rowCount()
        self.sourcelenth = self.ui.treeView.model().rowCount()
        if self.outlenth > self.sourcelenth:
            self.warn()
        elif self.outlenth < self.sourcelenth:
            self.warn1()
        else:
            self.num = 0
            while self.num < self.outlenth:
                self.renaming(self.num)

                self.num += 1
                if self.num == self.outlenth:
                    self.sucess()
                    self.close()
    def deletesourc(self):

        self.indexe = self.ui.treeView.selectionModel().selectedIndexes()
        try:
            self.row = self.indexe[0].row()
        except:
            pass

        else:

            self.first_cell_selected = self.ui.treeView.model().removeRow(self.row)
    def deleteout(self):

        self.indexes = self.ui.treeView_2.selectionModel().selectedIndexes()
        try:
            self.rows = self.indexes[0].row()

        except:
            pass

        else:

            self.first_cell_selecteds = self.ui.treeView_2.model().removeRow(self.rows)

    def selectionsource(self):
        self.indexe = self.ui.treeView.selectionModel().selectedIndexes()
        try:
            self.row = self.indexe[0].row()
        except:
            self.loginerror()

        else:
            self.column = self.ui.treeView.model().index(self.row, 0)
            self.first_cell_selected = self.ui.treeView.model().data(self.column, QtCore.Qt.DisplayRole)
            return self.first_cell_selected
    def deletor(self,ok):

        self.ui.treeView_2.model().removeRow(ok)

    def inserers(self,ok,loki):

        self.ui.treeView_2.model().insertRow(ok, loki)

    def deletorsource(self, ok):

        self.ui.treeView.model().removeRow(ok)

    def inserersource(self, ok, loki):

        self.ui.treeView.model().insertRow(ok, loki)
    def selectionoutputdown(self):
        self.indexe = self.ui.treeView_2.selectionModel().selectedIndexes()
        try:
            self.row = self.indexe[0].row()
        except:
            pass

        else:

            self.column = self.ui.treeView_2.model().index(self.row, 0)
            self.first_cell_selected = self.ui.treeView_2.model().data(self.column, QtCore.Qt.DisplayRole)
            self.firstitem = QtGui.QStandardItem(self.first_cell_selected)
            self.rowabovekk = int(self.row) + 1
            if self.rowabovekk >= 0:
                self.columnabove = self.ui.treeView_2.model().index(self.rowabovekk, 0)
                self.second_cell = self.ui.treeView_2.model().data(self.columnabove, QtCore.Qt.DisplayRole)
                self.seconditem = QtGui.QStandardItem(self.second_cell)
                self.deletor(self.row)
                self.deletor(self.row)

                self.inserers(self.row,self.firstitem)
                self.inserers(self.row, self.seconditem)
    def selectionoutputup(self):
        self.indexe = self.ui.treeView_2.selectionModel().selectedIndexes()
        try:
            self.row = self.indexe[0].row()
        except:
            pass

        else:

            self.column = self.ui.treeView_2.model().index(self.row, 0)
            self.first_cell_selected = self.ui.treeView_2.model().data(self.column, QtCore.Qt.DisplayRole)
            self.firstitem = QtGui.QStandardItem(self.first_cell_selected)
            self.rowabovekk = int(self.row) - 1
            if self.rowabovekk >= 0:
                self.columnabove = self.ui.treeView_2.model().index(self.rowabovekk, 0)
                self.second_cell = self.ui.treeView_2.model().data(self.columnabove, QtCore.Qt.DisplayRole)
                self.seconditem = QtGui.QStandardItem(self.second_cell)
                self.deletor(self.rowabovekk)
                self.deletor(self.rowabovekk)

                self.inserers(self.rowabovekk,self.seconditem)
                self.inserers(self.rowabovekk, self.firstitem)
    def selectionsourceup(self):
        self.indexe = self.ui.treeView.selectionModel().selectedIndexes()
        try:
            self.row = self.indexe[0].row()
        except:
            pass

        else:

            self.column = self.ui.treeView.model().index(self.row, 0)
            self.first_cell_selected = self.ui.treeView.model().data(self.column, QtCore.Qt.DisplayRole)
            self.firstitem = QtGui.QStandardItem(self.first_cell_selected)
            self.rowabovekk = int(self.row) - 1
            if self.rowabovekk >= 0:
                self.columnabove = self.ui.treeView.model().index(self.rowabovekk, 0)
                self.second_cell = self.ui.treeView.model().data(self.columnabove, QtCore.Qt.DisplayRole)
                self.seconditem = QtGui.QStandardItem(self.second_cell)
                self.deletorsource(self.rowabovekk)
                self.deletorsource(self.rowabovekk)

                self.inserersource(self.rowabovekk,self.seconditem)
                self.inserersource(self.rowabovekk, self.firstitem)
    def selectionsourcedown(self):
        self.indexe = self.ui.treeView.selectionModel().selectedIndexes()
        try:
            self.row = self.indexe[0].row()
        except:
            pass

        else:

            self.column = self.ui.treeView.model().index(self.row, 0)
            self.first_cell_selected = self.ui.treeView.model().data(self.column, QtCore.Qt.DisplayRole)
            self.firstitem = QtGui.QStandardItem(self.first_cell_selected)
            self.rowabovekk = int(self.row) + 1
            if self.rowabovekk >= 0:
                self.columnabove = self.ui.treeView.model().index(self.rowabovekk, 0)
                self.second_cell = self.ui.treeView.model().data(self.columnabove, QtCore.Qt.DisplayRole)
                self.seconditem = QtGui.QStandardItem(self.second_cell)
                self.deletorsource(self.row)
                self.deletorsource(self.row)

                self.inserersource(self.row, self.firstitem)
                self.inserersource(self.row, self.seconditem)


    def data(self):
        self.items_model = QtGui.QStandardItemModel()
        self.ui.treeView.setModel(self.items_model)
        self.ui.treeView.model().clear()

        self.header = (['Sources'])
        self.ui.treeView.model().setHorizontalHeaderLabels(self.header)
        self.font = QtGui.QFont()
        self.font.setWeight(QtGui.QFont.Bold)
        for self.source in sources:
            self.name = QtGui.QStandardItem(self.source)
            self.ui.treeView.model().appendRow([self.name])

        self.items_models = QtGui.QStandardItemModel()
        self.ui.treeView_2.setModel(self.items_models)
        self.ui.treeView_2.model().clear()
        self.headers = (['Output'])
        self.ui.treeView_2.model().setHorizontalHeaderLabels(self.headers)


        for self.out in output:
            self.outp = QtGui.QStandardItem(self.out)
            self.ui.treeView_2.model().appendRow([self.outp])



    def __init__(self):
        super(rename, self).__init__()

        self.ui = renameod()
        self.ui.setupUi(self)
        self.setWindowTitle('Renaming Window')
        self.setWindowIcon(QtGui.QIcon('1.png'))

        self.ui.pushButton_6.clicked.connect(self.deletesourc)
        self.ui.pushButton_7.clicked.connect(self.deleteout)
        self.ui.pushButton_3.clicked.connect(self.selectionoutputup)
        self.ui.pushButton_2.clicked.connect(self.selectionsourceup)
        self.ui.pushButton_4.clicked.connect(self.selectionoutputdown)
        self.ui.pushButton.clicked.connect(self.selectionsourcedown)
        self.ui.pushButton_5.clicked.connect(self.rename)
        self.data()

class ApplicationWindow(QtWidgets.QMainWindow):
    output = []
    sources = []
    temp  = []

    def dwonloaderror(self):
        self.fileerror = errors[1]
        QMessageBox.about(self, "extraction error",
                          "due site error cloadflare page loaded {} corrupted file downloaded".format(self.fileerror))

    def deepmoed(self):
        QMessageBox.about(self, "deep search",
                          "deep mode seach activated,there is chance it get wrong series please check")

    def nosub(self):
        QMessageBox.about(self, "no  luck ", "no subtitle have being found sorry ")
    def closer(self):
        self.read = prog[0]
        self.errorchers = int(errors[0])
        if self.errorchers == 3:
            self.deepmoed()
            errors.insert(0,0)
        elif self.errorchers == 1:
            self.nosub()
            errors.insert(0, 0)
        elif self.errorchers == 2:
            self.dwonloaderror()
            errors.insert(0, 0)
        if self.read == 100:
            self.splash.hide()

            prog.clear()
            prog.insert(0,0)

    def subscene(self):
        self.splash = splash()
        self.splash.ui.centralwidget.show()
        self.splash.show()
        self.label = QtWidgets.QLabel(self.splash.ui.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(281, 211))
        self.label.setStyleSheet("image: url(1.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.splash.ui.gridLayout.addWidget(self.label, 0, 0, 1, 1)




        self.centralwidget = QtWidgets.QMainWindow()
        self.timer = QtCore.QTimer(self.centralwidget)
        self.timer.timeout.connect(self.closer)
        self.timer.start(100)
        self.taska = threading.Thread(target=self.subscensse)
        self.taska.start()


    def someerror(self):
        QMessageBox.about(self, "error", "We couldn't find Series with that ID")
        prog.insert(0,100)

    def someerror1(self):
        QMessageBox.about(self, "error", "No files found")
        prog.insert(0,100)
    def someerror2(self):
        QMessageBox.about(self, "error", "Please enter proper season number")
        prog.insert(0,100)
    def subscensse(self):
        output.clear()
        sources.clear()
        self.output.clear()
        self.sources.clear()
        self.TVMAZEID = self.ui.lineEdit_3.text()
        if self.TVMAZEID == "":
            self.someerror()
        else:
            self.ex = ('.webm', '.mkv', '.flv', '.vob', '.ogv', '.drc', '.mng', '.avi', '.mov', '.qt', '.wmv', '.yuv',
                       '.rm', '.rmvb', '.asf', '.amv', '.mp4', '.m4p', '.m4v', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv',
                       '.mpg', '.mpeg', '.m2v', '.m4v', '.svi', '.3gp', '.3g2', '.mxf', '.roq', '.nsv', '.flv', '.f4v',
                       '.f4p', '.f4a', '.f4b')
            try:
                self.workdir = dir[0]
            except:
                self.someerror1()
            else:
                self.u = 0
                for self.files in os.listdir(self.workdir):
                    if self.files.endswith(self.ex):
                        sources.append(self.files)

            self.season = self.ui.lineEdit_4.text()
            if self.season == "":
                self.someerror2()
            else:

                self.show = tvm.get_show(maze_id=self.TVMAZEID, embed='episodes')
                output.clear()
                self.tvmazeid()
                for self.episode in self.show[int(self.season)]:
                    if self.episode not in self.output:
                        self.output.append(self.episode.title)
                        self.tester()
                        self.counter()
                        self.kind = str(self.subformatreader())


                        self.hearing = self.ui.checkBox.isChecked()
                        self.languauge = self.ui.comboBox.currentText()

                if (len(sources) != 0) and (self.TVMAZEID != "") and (self.season != ""):
                    subscenes(name=str(self.ui.lineEdit_2.text()),season=str(self.ui.lineEdit_4.text()),kind=self.kind,hearing=self.hearing,langugage=self.languauge,tt=self)

    def tvmaze(self):
        self.showname = self.ui.lineEdit_2.text()
        TVMAZE(name=self.showname,tt=self)
    def tvmazeid(self):
        self.id = self.ui.lineEdit_3.text()
        TVMAZE(id=self.id,tt=self)
    def flashback(self,name,id):
        self.ui.lineEdit_2.setText(name)
        self.id = str(id)
        self.ui.lineEdit_3.setText(self.id )

    def preview(self):
        self.previews = rename()
        self.previews.show()
    def browse(self):
        dir.clear()

        self.file = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.dir = str(self.file)
        dir.insert(0,self.dir)

    def counter(self):
        self.shownames = self.ui.lineEdit_2.text()
        self.count = self.seasonreader()
        self.startep = self.ui.lineEdit.text()
        self.outlenth = len(self.output)
        self.fronttag = self.ui.lineEdit_5.text()
        self.endtag = self.ui.lineEdit_6.text()
        self.outseason = self.ui.lineEdit_4.text()
        if int(self.startep) == "" or int(self.startep) < 1:
            self.startep = 1
        if self.count == "one":

            self.cu = 0

            while self.cu < self.outlenth:
                self.epcount = int(self.cu) + int(self.startep)
                self.result = self.fronttag + " " + self.shownames + " " +  str("{0:0=2d}".format(self.epcount)) + " " + str(self.output[self.cu]) + " " + self.endtag
                self.result  = self.result.strip()
                if self.result not in output:
                    output.append(self.result)
                self.cu += 1

        elif self.count == "two":

            self.cu = 0

            while self.cu < self.outlenth:
                self.epcount = self.cu + 1
                self.result = self.fronttag + " " + self.shownames + " " + str("{0:0=2d}".format(int(self.outseason))) + "x" + str("{0:0=2d}".format(self.epcount)) + " " + str(
                    self.output[self.cu]) + " " + self.endtag
                self.result = self.result.strip()
                if self.result not in output:
                    output.append(self.result)
                self.cu += 1
        else:

            self.cu = 0

            while self.cu < self.outlenth:
                self.epcount = self.cu + 1
                self.result = self.fronttag + " " + self.shownames + " " + "S" + str("{0:0=2d}".format(int(self.outseason))) + "E" + str("{0:0=2d}".format(self.epcount)) + " " + str(
                    self.output[self.cu]) + " " + self.endtag
                self.result = self.result.strip()
                if self.result not in output:
                    output.append(self.result)
                self.cu += 1

    def addcombo(self):
        self.lan = ['English','Akan', 'Amharic', 'Arabic', 'Assamese', 'Awadhi', 'Azerbaijani', 'Balochi', 'Bangla', 'Belarusian', 'Bengali', 'Bhojpuri', 'Brazillian Portuguese', 'Bulgarian/ English', 'Burmese', 'Cantonese', 'Catalan', 'Cebuano', 'Chewa', 'Chhattisgarhi', 'Chinese BG code', 'Chittagonian', 'Czech', 'Deccan', 'Dhundhari', 'Dutch', 'Dutch/ English', 'Eastern Min', 'English', 'English/ German', 'Farsi/Persian', 'Filipino', 'French', 'Fula', 'Fuzhounese', 'Gan Chinese', 'German', 'Greek', 'Greenlandic', 'Gujarati', 'Haitian Creole', 'Hakka', 'Haryanvi', 'Hausa', 'Hiligaynon', 'Hindi[a]', 'Hmong', 'Hokkien', 'Hunanese', 'Hungarian', 'Hungarian/ English', 'Igbo', 'Ilocano', 'Ilonggo', 'Indonesian', 'Italian', 'Japanese', 'Javanese', 'Jin', 'Kannada', 'Kazakh', 'Khmer', 'Kinyarwanda', 'Kirundi', 'Konkani', 'Korean', 'Kurdish', 'Madurese', 'Magahi', 'Maithili', 'Malagasy', 'Malay', 'Malayalam', 'Malaysian', 'Mandarin', 'Marathi', 'Marwari', 'Mossi', 'Nepali', 'Northern Min', 'Odia', 'Oriya', 'Oromo', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Quechua', 'Romanian', 'Russian', 'Saraiki', 'Serbo-Croatian', 'Shanghainese', 'Shona', 'Sindhi', 'Sinhalese', 'Somali', 'Southern Min', 'Spanish', 'Sundanese', 'Swedish', 'Sylheti', 'Tagalog', 'Tamil', 'Telugu', 'Teochew)', 'Thai', 'Turkish', 'Turkmen', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Visayan', 'Visayan', 'Wu', 'Xhosa', 'Xiang', 'Yoruba', 'Yue', 'Zhuang', 'Zulu']

        for self.lans in self.lan:
            self.ui.comboBox.addItem(self.lans)

    def seasonreader(self):
        if self.ui.radioButton_4.isChecked() == True:
            return 'one'
        elif self.ui.radioButton_5.isChecked() == True:
            return 'two'
        else:
            return "three"
    def subformatreader(self):
        if self.ui.radioButton.isChecked() == True:
            return 'one'
        elif self.ui.radioButton_2.isChecked() == True:
            return 'two'
        elif self.ui.radioButton_3.isChecked() == True:
            return 'three'
        else:
            return "four"
    def tags(self):
        self.fronttag = self.ui.lineEdit_5.text()
        self.endtag = self.ui.lineEdit_6.text()
        self.format = self.seasonreader()

        if self.format == 'one':
            self.out = self.fronttag + ' ' + "dexter" + ' 01 ' +"Crocodile" + ' ' + self.endtag
        elif self.format == 'two':
            self.out = self.fronttag + ' ' + "dexter" + ' 01x01 ' + "Crocodile" + ' ' + self.endtag
        else:
            self.out = self.fronttag + ' ' + "dexter" + ' S01E01 ' + "Crocodile" + ' ' + self.endtag
        self.out = "    " +  self.out
        self.ui.label_2.setText(self.out)
    def previewworks(self):
        output.clear()
        sources.clear()
        self.output.clear()
        self.sources.clear()
        self.TVMAZEID = self.ui.lineEdit_3.text()
        if self.TVMAZEID == "":
            self.someerror()
        else:
            self.ex = ('.webm', '.mkv', '.flv', '.vob', '.ogv', '.drc', '.mng', '.avi', '.mov', '.qt', '.wmv', '.yuv',
                       '.rm', '.rmvb', '.asf', '.amv', '.mp4', '.m4p', '.m4v', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv',
                       '.mpg', '.mpeg', '.m2v', '.m4v', '.svi', '.3gp', '.3g2', '.mxf', '.roq', '.nsv', '.flv', '.f4v',
                       '.f4p', '.f4a', '.f4b')
            try:
                self.workdir = dir[0]
            except:
                self.someerror1()
            else:
                self.u = 0
                for self.files in os.listdir(self.workdir):
                    if self.files.endswith(self.ex):
                        sources.append(self.files)

            self.season = self.ui.lineEdit_4.text()
            if self.season == "":
                self.someerror2()
            else:

                self.show = tvm.get_show(maze_id=self.TVMAZEID, embed='episodes')
                output.clear()
                self.tvmazeid()
                for self.episode in self.show[int(self.season)]:
                    if self.episode not in self.output:
                        self.output.append(self.episode.title)
                        self.tester()
                        self.counter()


                        self.preview()










    def tester(self):

        sources.sort(key=self.natural_keys)




    def atoi(self, text):
        return int(text) if text.isdigit() else text

    def natural_keys(self, text):

        return [self.atoi(c) for c in re.split('(\d+)', text)]



    def __init__(self):

        super(ApplicationWindow, self).__init__()

        self.ui = mainos()
        self.ui.setupUi(self)
        self.setWindowTitle('Naming')
        self.setWindowIcon(QtGui.QIcon('1.png'))
        self.ui.lineEdit.setPlaceholderText("Start Episode \n only affect 01,02,03")
        self.ui.lineEdit_2.setPlaceholderText("Series Name")
        self.ui.lineEdit_3.setPlaceholderText("IMDB or TvMaze ID")
        self.ui.lineEdit_4.setPlaceholderText("Season  Number")
        self.ui.lineEdit_5.setPlaceholderText("Front Tags")
        self.ui.lineEdit_6.setPlaceholderText("End Tags")
        self.ui.lineEdit.setText('1')
        self.ui.lineEdit.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_4.setValidator(QtGui.QIntValidator())
        self.ui.pushButton_6.clicked.connect(self.previewworks)
        self.ui.pushButton_3.clicked.connect(self.tvmaze)
        self.ui.pushButton_5.clicked.connect(self.tvmazeid)
        self.ui.pushButton_2.clicked.connect(self.browse)
        self.ui.pushButton.clicked.connect(self.subscene)
        self.number_group = QtWidgets.QButtonGroup()
        self.number2_group = QtWidgets.QButtonGroup(self)
        self.ui.lineEdit_4.setText("1")

        self.number_group.addButton(self.ui.radioButton)
        self.number_group.addButton(self.ui.radioButton_2)
        self.number_group.addButton(self.ui.radioButton_3)
        self.number_group.addButton(self.ui.radioButton_7)

        self.number2_group.addButton(self.ui.radioButton_4)
        self.number2_group.addButton(self.ui.radioButton_5)
        self.number2_group.addButton(self.ui.radioButton_6)

        self.ui.radioButton.setChecked(True)
        self.ui.radioButton_4.setChecked(True)
        self.ui.pushButton_4.clicked.connect(self.tags)

        self.addcombo()
class splash(QtWidgets.QMainWindow):
    def reading(self):
        self.read = prog[0]

        self.ui.progressBar.setValue(self.read)

    def __init__(self):

        super(splash, self).__init__()

        self.ui = sp()
        self.ui.setupUi(self)
        self.setWindowTitle('looking for subtitle ')
        self.setWindowIcon(QtGui.QIcon('1.png'))
        self.ui.label.setStyleSheet("image: url(1.png);")
        self.ui.progressBar.setValue(0)
        self.centralwidget = QtWidgets.QMainWindow()
        self.timeree = QtCore.QTimer(self.centralwidget)
        self.timeree.timeout.connect(self.reading)
        self.timeree.start(500)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())





if __name__ == "__main__":
    tvm = pytvmaze.TVMaze()
    main()
