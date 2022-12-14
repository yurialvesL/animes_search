# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'informations.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        MainWindow.setStyleSheet("background-color: rgb(84, 84, 84);\n"
"/*background-image:url(C:/Users/Yuri/PycharmProject/anime/img/wallpaper.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.QFrame_Information = QtWidgets.QFrame(self.centralwidget)
        self.QFrame_Information.setStyleSheet("Border-radius:15px;\n"
"Border-color:solid 15px white;\n"
"background-color: rgb(0, 0, 0);")
        self.QFrame_Information.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.QFrame_Information.setFrameShadow(QtWidgets.QFrame.Raised)
        self.QFrame_Information.setObjectName("QFrame_Information")
        self.scrollArea = QtWidgets.QScrollArea(self.QFrame_Information)
        self.scrollArea.setGeometry(QtCore.QRect(10, 60, 601, 631))
        self.scrollArea.setStyleSheet("\n"
"/*scroll vertical*/\n"
"QScrollBar:vertical{\n"
"border:none;\n"
"background-color: rgb(59, 59, 90);\n"
"width:14px;\n"
"margin: 15px 0 15px 0;\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"/* handle bar  vertical*/\n"
"QScrollBar::handle:vertical{\n"
"background-color: rgb(80, 80, 122);\n"
"min-heinght:10px;\n"
"border-radius:7px;\n"
"\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"background-color: rgb(0, 0, 255);\n"
"\n"
"}\n"
"QscollBar::handle:vertical:pressed {\n"
"background-color:rgb(185,0,92);\n"
"\n"
"}\n"
"")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 584, 978))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setMinimumSize(QtCore.QSize(350, 960))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 161, 48))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lbl_romaji = QtWidgets.QLabel(self.frame_2)
        self.lbl_romaji.setGeometry(QtCore.QRect(230, 50, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(14)
        self.lbl_romaji.setFont(font)
        self.lbl_romaji.setStyleSheet("border-bottom: 5px solid black;\n"
"border-radius:none;")
        self.lbl_romaji.setObjectName("lbl_romaji")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(30, 110, 153, 48))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lbl_english = QtWidgets.QLabel(self.frame_2)
        self.lbl_english.setGeometry(QtCore.QRect(230, 110, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(14)
        self.lbl_english.setFont(font)
        self.lbl_english.setStyleSheet("border-bottom: 5px solid black;\n"
"border-radius:none;")
        self.lbl_english.setObjectName("lbl_english")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(30, 170, 123, 48))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lbl_launch_date = QtWidgets.QLabel(self.frame_2)
        self.lbl_launch_date.setGeometry(QtCore.QRect(230, 170, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(14)
        self.lbl_launch_date.setFont(font)
        self.lbl_launch_date.setStyleSheet("border-bottom: 5px solid black;\n"
"border-radius:none;")
        self.lbl_launch_date.setObjectName("lbl_launch_date")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(20, 40, 191, 181))
        self.label_6.setStyleSheet("border: 4px solid black;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(220, 40, 341, 51))
        self.label_7.setStyleSheet("border: 4px solid black")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(220, 100, 341, 51))
        self.label_8.setStyleSheet("border: 4px solid black")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(220, 160, 341, 51))
        self.label_9.setStyleSheet("border: 4px solid black")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(20, 240, 291, 181))
        self.label_10.setStyleSheet("border: 4px solid black;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(30, 250, 265, 48))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(30, 320, 238, 48))
        self.label_12.setMinimumSize(QtCore.QSize(238, 48))
        self.label_12.setMaximumSize(QtCore.QSize(238, 48))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(30, 370, 87, 48))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(20)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(320, 240, 241, 51))
        self.label_14.setStyleSheet("border: 4px solid black")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.lbl_temp_launch = QtWidgets.QLabel(self.frame_2)
        self.lbl_temp_launch.setGeometry(QtCore.QRect(330, 250, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(14)
        self.lbl_temp_launch.setFont(font)
        self.lbl_temp_launch.setStyleSheet("border-bottom: 5px solid black;\n"
"border-radius:none;")
        self.lbl_temp_launch.setObjectName("lbl_temp_launch")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(320, 310, 241, 51))
        self.label_15.setStyleSheet("border: 4px solid black")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.lbl_qtd_ep = QtWidgets.QLabel(self.frame_2)
        self.lbl_qtd_ep.setGeometry(QtCore.QRect(330, 320, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(14)
        self.lbl_qtd_ep.setFont(font)
        self.lbl_qtd_ep.setStyleSheet("border-bottom: 5px solid black;\n"
"border-radius:none;")
        self.lbl_qtd_ep.setObjectName("lbl_qtd_ep")
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        self.label_16.setGeometry(QtCore.QRect(320, 370, 241, 51))
        self.label_16.setStyleSheet("border: 4px solid black")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.lbl_genre = QtWidgets.QLabel(self.frame_2)
        self.lbl_genre.setGeometry(QtCore.QRect(330, 380, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(14)
        self.lbl_genre.setFont(font)
        self.lbl_genre.setStyleSheet("border-bottom: 5px solid black;\n"
"border-radius:none;")
        self.lbl_genre.setObjectName("lbl_genre")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setGeometry(QtCore.QRect(20, 440, 541, 491))
        self.label_17.setStyleSheet("border: 4px solid black;")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.tb_sinopse = QtWidgets.QTextBrowser(self.frame_2)
        self.tb_sinopse.setGeometry(QtCore.QRect(40, 500, 501, 421))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.tb_sinopse.setFont(font)
        self.tb_sinopse.setObjectName("tb_sinopse")
        self.label_18 = QtWidgets.QLabel(self.frame_2)
        self.label_18.setGeometry(QtCore.QRect(40, 450, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(20)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_9.raise_()
        self.label_8.raise_()
        self.label_7.raise_()
        self.label_6.raise_()
        self.label_3.raise_()
        self.lbl_romaji.raise_()
        self.label_4.raise_()
        self.lbl_english.raise_()
        self.label_5.raise_()
        self.lbl_launch_date.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.lbl_temp_launch.raise_()
        self.label_15.raise_()
        self.lbl_qtd_ep.raise_()
        self.label_16.raise_()
        self.lbl_genre.raise_()
        self.label_17.raise_()
        self.tb_sinopse.raise_()
        self.label_18.raise_()
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_2 = QtWidgets.QLabel(self.QFrame_Information)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.QFrame_Information)
        self.frame.setGeometry(QtCore.QRect(650, 10, 628, 681))
        self.frame.setStyleSheet("border-radius:15px;\n"
"background-color:black;\n"
"background-image:none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_animage = QtWidgets.QLabel(self.frame)
        self.lbl_animage.setGeometry(QtCore.QRect(9, 9, 567, 500))
        self.lbl_animage.setMinimumSize(QtCore.QSize(567, 500))
        self.lbl_animage.setMaximumSize(QtCore.QSize(567, 500))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(26)
        self.lbl_animage.setFont(font)
        self.lbl_animage.setStyleSheet("background-image: url(C:/Users/Yuri/PycharmProject/anime/img/kaminomizoshirusekai.jpg);\n"
"background-size: 600px 300px;\n"
"background-repeat: no-repeat;")
        self.lbl_animage.setText("")
        self.lbl_animage.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_animage.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_animage.setObjectName("lbl_animage")
        self.lbl_titulo = QtWidgets.QLabel(self.frame)
        self.lbl_titulo.setGeometry(QtCore.QRect(160, 510, 289, 58))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_titulo.setStyleSheet("Border-bottom: 2px solid white;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:0px;")
        self.lbl_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.btn_voltar = QtWidgets.QPushButton(self.frame)
        self.btn_voltar.setGeometry(QtCore.QRect(494, 630, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(14)
        font.setUnderline(False)
        self.btn_voltar.setFont(font)
        self.btn_voltar.setStyleSheet("color: rgb(255, 255, 255);\n"
"border:1px solid white;\n"
"border-radius:20px;\n"
"\n"
"QPushButton::handle {\n"
"    background-color: rgb(224, 0, 0);\n"
"    border-style: inset;\n"
"}")
        self.btn_voltar.setObjectName("btn_voltar")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(20, 590, 70, 61))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(26)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.label_19.setObjectName("label_19")
        self.lbl_nota = QtWidgets.QLabel(self.frame)
        self.lbl_nota.setGeometry(QtCore.QRect(100, 600, 30, 51))
        font = QtGui.QFont()
        font.setFamily("Bangers")
        font.setPointSize(22)
        self.lbl_nota.setFont(font)
        self.lbl_nota.setStyleSheet("color:white;")
        self.lbl_nota.setObjectName("lbl_nota")
        self.horizontalLayout.addWidget(self.QFrame_Information)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Anime description"))
        self.centralwidget.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Nome em Romaji:"))
        self.lbl_romaji.setText(_translate("MainWindow", "Kami nomi zo shiru sekai "))
        self.label_4.setText(_translate("MainWindow", "Nome em Ingl??s:"))
        self.lbl_english.setText(_translate("MainWindow", "The World God Only Knows"))
        self.label_5.setText(_translate("MainWindow", "Lan??amento:"))
        self.lbl_launch_date.setText(_translate("MainWindow", "7/05/2016"))
        self.label_11.setText(_translate("MainWindow", "Temporada do lan??amento:"))
        self.label_12.setText(_translate("MainWindow", "Quantidade de epis??dios:"))
        self.label_13.setText(_translate("MainWindow", "G??neros:"))
        self.lbl_temp_launch.setText(_translate("MainWindow", "Winter"))
        self.lbl_qtd_ep.setText(_translate("MainWindow", "400"))
        self.lbl_genre.setText(_translate("MainWindow", "<html><head/><body><p>a????o, com??dia, romance,supernatural</p></body></html>"))
        self.tb_sinopse.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">O deus menor Yato est?? com pouca sorte. Farto de seu estilo de vida pregui??oso, seu parceiro desiste abruptamente. Ele n??o tem dinheiro, nem adoradores, nem santu??rio para chamar de lar. Mas justamente quando as coisas come??am a parecer sem esperan??a, um acidente de ??nibus o for??a a cruzar com Hiyori Iki, uma doce e alegre colegial. Ap??s o acidente, a alma de Hiyori tem o mau h??bito de escorregar para fora de seu corpo, e depois de pedir a ajuda de Yato para traz??-la de volta ao normal, ela come??a a cair no mundo dos esp??ritos e deuses.&lt;br&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;br&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mas Hiyori n??o ?? a ??nica que est?? de olho em Yato. Um deus do passado de Yato est?? de volta e ele n??o est?? interessado em um reencontro amig??vel.</p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "Sinopse:"))
        self.label_2.setText(_translate("MainWindow", "Informa????es:"))
        self.lbl_titulo.setText(_translate("MainWindow", "Kami Nomi Zo Shiru Sekai"))
        self.btn_voltar.setText(_translate("MainWindow", "Voltar"))
        self.label_19.setText(_translate("MainWindow", "Nota:"))
        self.lbl_nota.setText(_translate("MainWindow", "85"))
