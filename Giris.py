import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Kitap import Ui_KitapMainWindow

from Kayıt import Ui_KayıtMainWindow

import sqlite3 as sql

class Ui_MainWindow(object):

    def ac(self):
        self.window =QtWidgets.QMainWindow()
        self.uiK = Ui_KitapMainWindow()
        self.uiK.setupUi(self.window)
        conn = sql.connect("Kullanıcılar.db")
        curs = conn.cursor()
        veriler = curs.execute("SELECT*FROM kullanıcı")

        for i in veriler:

            if self.kullanci_edit.text() == i[0] and self.sifre_edit.text() == i[1]:
                self.window.show()
                penAna.hide()
            else:
                self.btn_giris.clicked.connect(self.uyarı)


                #self.statusbar.showMessage("Kullanıcı adı veya parola yanlış!")

    def uyarı(self):
        mesaj = QMessageBox.warning(self, "uyarı", "Kullanıcı adı veya parola yanlış!",QMessageBox.Ok | QMessageBox.Cancel)

    def kayitOl(self):
        self.window = QtWidgets.QMainWindow()
        self.uiKayıt = Ui_KayıtMainWindow()
        self.uiKayıt.setupUi(self.window)
        self.window.show()
        penAna.hide()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.kullanci_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.kullanci_edit.setGeometry(QtCore.QRect(210, 90, 201, 21))
        self.kullanci_edit.setObjectName("kullanci_edit")
        self.sifre_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.sifre_edit.setGeometry(QtCore.QRect(210, 140, 201, 21))
        self.sifre_edit.setObjectName("sifre_edit")
        self.btn_giris = QtWidgets.QPushButton(self.centralwidget)
        self.btn_giris.setGeometry(QtCore.QRect(210, 200, 75, 23))
        self.btn_giris.setObjectName("btn_giris")
        self.btn_giris.clicked.connect(self.ac)
        self.btn_kayitOl = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kayitOl.setGeometry(QtCore.QRect(340, 200, 75, 23))
        self.btn_kayitOl.setObjectName("btn_kayitOl")
        self.btn_kayitOl.clicked.connect(self.kayitOl)
        self.kullanci_label = QtWidgets.QLabel(self.centralwidget)
        self.kullanci_label.setGeometry(QtCore.QRect(100, 90, 91, 21))
        self.kullanci_label.setObjectName("kullanci_label")
        self.sifre_label = QtWidgets.QLabel(self.centralwidget)
        self.sifre_label.setGeometry(QtCore.QRect(100, 140, 91, 16))
        self.sifre_label.setObjectName("sifre_label")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_giris.setText(_translate("MainWindow", "Giriş Yap"))
        self.btn_kayitOl.setText(_translate("MainWindow", "Kayıt Ol"))
        self.kullanci_label.setText(_translate("MainWindow", "Kullanıcı Adı :"))
        self.sifre_label.setText(_translate("MainWindow", "Şifre :"))

uyg = QtWidgets.QApplication(sys.argv)
penAna = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()
uyg.exec_()