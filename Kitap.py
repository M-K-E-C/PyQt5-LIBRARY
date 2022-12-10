from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql

from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem

conn = sql.connect("Kitaplar.db")
imlec = conn.cursor()
tabloOluştur = imlec.execute("CREATE TABLE IF NOT EXISTS kitap(KitapAdı, YazarAdı, SayfaSayısı)")

class Ui_KitapMainWindow(object):

    def ekle(self):
        kitap_adi = self.kitap_adi_edit.text().upper()
        yazar_adi = self.yazar_adi_edit.text().upper()
        sayfa_sayisi = self.sayfa_sayisi_edit.text().upper()
        deger = (kitap_adi,yazar_adi,sayfa_sayisi)
        veri = "INSERT INTO kitap(KitapAdı, YazarAdı, SayfaSayısı) VALUES(?,?,?)"
        imlec.execute(veri,deger)
        conn.commit()
        self.listele()


    def sil(self):
        veriler = imlec.execute("SELECT*FROM kitap")
        kitap_adi = self.kitap_adi_edit.text().upper()
        silinecek_veri =""

        for i in veriler:
            if kitap_adi == i[0]:
                silinecek_veri = i[0]

        a = "DELETE FROM kitap WHERE kitapAdı = ?"
        imlec.execute(a, (silinecek_veri,))
        conn.commit()
        self.listele()

    def listele(self):
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(('KİTAP ADI','YAZAR ADI',' SAYFA SAYISI'))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        data = imlec.execute("SELECT*FROM kitap")
        for satirİndeks,satirVeri in enumerate(data):
            for sutunİndeks,sutunVeri in enumerate(satirVeri):
                self.tableWidget.setItem(satirİndeks,sutunİndeks,QTableWidgetItem(str(sutunVeri)))

        kayitSayisi = imlec.execute("SELECT KitapAdı FROM kitap")
        liste = []
        for i in kayitSayisi:
            liste.append(i[0])
        a = len(liste)
        self.lbl_kayt_sayisi.setText(str(a))

    def KitapAra(self):
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(('KİTAP ADI','YAZAR ADI',' SAYFA SAYISI'))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        aranacak_kitap = self.kitap_adi_edit.text().upper()
        sorgu = "SELECT*FROM kitap WHERE KitapAdı=? "
        veriler = imlec.execute(sorgu,(aranacak_kitap,))
        for satırİndeks, satırVeri in enumerate(veriler):
            for sutunİndeks, sutunVeri in enumerate(satırVeri):
                self.tableWidget.setItem(satırİndeks, sutunİndeks, QTableWidgetItem(str(sutunVeri)))

    def yazarAra(self):
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(('KİTAP ADI', 'YAZAR ADI', ' SAYFA SAYISI'))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        aranacak_yazar = self.yazar_adi_edit.text().upper()
        sorgu = "SELECT*FROM kitap WHERE YazarAdı=? "
        veriler = imlec.execute(sorgu, (aranacak_yazar,))
        for satırİndeks, satırVeri in enumerate(veriler):
            for sutunİndeks, sutunVeri in enumerate(satırVeri):
                self.tableWidget.setItem(satırİndeks, sutunİndeks, QTableWidgetItem(str(sutunVeri)))



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 641)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.kitap_adi_label = QtWidgets.QLabel(self.centralwidget)
        self.kitap_adi_label.setGeometry(QtCore.QRect(181, 71, 67, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.kitap_adi_label.setFont(font)
        self.kitap_adi_label.setObjectName("kitap_adi_label")
        self.yazar_adi_label = QtWidgets.QLabel(self.centralwidget)
        self.yazar_adi_label.setGeometry(QtCore.QRect(181, 97, 72, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.yazar_adi_label.setFont(font)
        self.yazar_adi_label.setObjectName("yazar_adi_label")
        self.sayfa_sayisi_label = QtWidgets.QLabel(self.centralwidget)
        self.sayfa_sayisi_label.setGeometry(QtCore.QRect(181, 123, 87, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sayfa_sayisi_label.setFont(font)
        self.sayfa_sayisi_label.setObjectName("sayfa_sayisi_label")
        self.kitap_adi_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.kitap_adi_edit.setGeometry(QtCore.QRect(274, 71, 231, 20))
        self.kitap_adi_edit.setObjectName("kitap_adi_edit")
        self.yazar_adi_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.yazar_adi_edit.setGeometry(QtCore.QRect(274, 97, 231, 20))
        self.yazar_adi_edit.setObjectName("yazar_adi_edit")
        self.sayfa_sayisi_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.sayfa_sayisi_edit.setGeometry(QtCore.QRect(274, 123, 71, 20))
        self.sayfa_sayisi_edit.setObjectName("sayfa_sayisi_edit")
        self.btn_ekle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ekle.setGeometry(QtCore.QRect(120, 190, 75, 23))
        self.btn_ekle.setObjectName("btn_ekle")
        self.btn_ekle.clicked.connect(self.ekle)
        self.btn_sil = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sil.setGeometry(QtCore.QRect(220, 190, 75, 23))
        self.btn_sil.setObjectName("btn_sil")
        self.btn_sil.clicked.connect(self.sil)
        self.btn_listele = QtWidgets.QPushButton(self.centralwidget)
        self.btn_listele.setGeometry(QtCore.QRect(320, 190, 91, 23))
        self.btn_listele.setObjectName("btn_listele")
        self.btn_listele.clicked.connect(self.listele)
        self.btn_yazarAra = QtWidgets.QPushButton(self.centralwidget)
        self.btn_yazarAra.setGeometry(QtCore.QRect(430, 190, 75, 23))
        self.btn_yazarAra.setObjectName("btn_yazarAra")
        self.btn_yazarAra.clicked.connect(self.yazarAra)
        self.btn_kitapAra = QtWidgets.QPushButton(self.centralwidget)
        self.btn_kitapAra.setGeometry(QtCore.QRect(530, 190, 75, 23))
        self.btn_kitapAra.setObjectName("btn_kitapAra")
        self.btn_kitapAra.clicked.connect(self.KitapAra)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 240, 741, 271))
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 560, 101, 16))
        self.label.setObjectName("label")
        self.lbl_kayt_sayisi = QtWidgets.QLabel(self.centralwidget)
        self.lbl_kayt_sayisi.setGeometry(QtCore.QRect(150, 560, 47, 13))
        self.lbl_kayt_sayisi.setText("")
        self.lbl_kayt_sayisi.setObjectName("lbl_kayt_sayisi")
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
        self.kitap_adi_label.setText(_translate("MainWindow", "Kitap Adı :"))
        self.yazar_adi_label.setText(_translate("MainWindow", "Yazar Adı :"))
        self.sayfa_sayisi_label.setText(_translate("MainWindow", "Sayfa Sayısı :"))
        self.btn_ekle.setText(_translate("MainWindow", "Kitap Ekle"))
        self.btn_sil.setText(_translate("MainWindow", "Kitap Sil"))
        self.btn_listele.setText(_translate("MainWindow", "Kitapları Listele"))
        self.btn_yazarAra.setText(_translate("MainWindow", "Yazar Ara"))
        self.btn_kitapAra.setText(_translate("MainWindow", "Kitap Ara"))
        self.label.setText(_translate("MainWindow", "Kayıtlı Kitap Sayısı:"))
