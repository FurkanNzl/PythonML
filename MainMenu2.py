# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 491, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.btnVeriOku = QtWidgets.QPushButton(self.centralwidget)
        self.btnVeriOku.setGeometry(QtCore.QRect(30, 500, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnVeriOku.setFont(font)
        self.btnVeriOku.setAcceptDrops(False)
        self.btnVeriOku.setObjectName("btnVeriOku")
        self.btnTop = QtWidgets.QPushButton(self.centralwidget)
        self.btnTop.setGeometry(QtCore.QRect(544, 40, 141, 23))
        self.btnTop.setObjectName("btnTop")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(544, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.btnKmeans = QtWidgets.QPushButton(self.centralwidget)
        self.btnKmeans.setGeometry(QtCore.QRect(544, 120, 75, 23))
        self.btnKmeans.setObjectName("btnKmeans")
        self.btnAvg = QtWidgets.QPushButton(self.centralwidget)
        self.btnAvg.setGeometry(QtCore.QRect(30, 380, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.btnAvg.setFont(font)
        self.btnAvg.setObjectName("btnAvg")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(520, 180, 256, 192))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tableWidget, self.btnTop)
        MainWindow.setTabOrder(self.btnTop, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.btnKmeans)
        MainWindow.setTabOrder(self.btnKmeans, self.btnAvg)
        MainWindow.setTabOrder(self.btnAvg, self.btnVeriOku)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnVeriOku.setText(_translate("MainWindow", "Veri Oku"))
        self.btnTop.setText(_translate("MainWindow", "En Y??ksek De??erler Grafi??i"))
        self.pushButton.setText(_translate("MainWindow", "DBSCAN"))
        self.btnKmeans.setText(_translate("MainWindow", "KMeans"))
        self.btnAvg.setText(_translate("MainWindow", "Top Info"))
