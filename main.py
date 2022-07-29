import sys
import os
from templates.information import *
from templates.principal import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from AnilistPython import Anilist
from googletrans import Translator
from datetime import datetime

import requests

nome = ''


class Information(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowIcon(QIcon('img/esfera.ico'))
        self.btn_voltar.clicked.connect(self.back_principal)

    def dowload_animage(self, anime, link):  # donwload image from anime
        link = link.replace('medium', 'large')
        f = open(anime + ".jpg", 'wb')
        response = requests.get(link)
        f.write(response.content)
        f.close()

    def description(self, anime):  # sets the informations from anime
        anilist = Anilist()
        translator = Translator()
        generos = ''
        anime_dict = None


        anime_dict = anilist.get_anime(anime)


        self.setWindowTitle(anime)
        self.lbl_romaji.setText(anime_dict.get('name_romaji'))
        self.lbl_english.setText(anime_dict.get('name_english'))
        self.lbl_titulo.setText(anime_dict.get('name_romaji'))

        if anime_dict.get('airing_episodes') is None:
            self.lbl_qtd_ep.setText('Ainda em Lançamento')

        else:
            self.lbl_qtd_ep.setText(str(anime_dict.get('airing_episodes')))

        data = anime_dict.get('starting_time')
        data_str = datetime.strptime(data, '%m/%d/%Y')
        data_new = data_str.strftime('%d/%m/%Y')
        self.lbl_launch_date.setText(data_new)

        self.lbl_temp_launch.setText(anime_dict.get('season'))

        genres = " , ".join(str(x) for x in anime_dict.get('genres'))  # convert list of genres to string

        if 25 < len(genres) < 30: #adjust font-size if len > 25
            self.lbl_genre.setStyleSheet('font-size:17px; border-bottom:5px solid black; border-radius:none;')
            self.lbl_genre.setText(genres)
        elif len(genres) >=30:
            self.lbl_genre.setStyleSheet('font-size:15px; border-bottom:5px solid black; border-radius:none;')
            self.lbl_genre.setText(genres[:35])
        else:
            self.lbl_genre.setText(genres)

        try:
            traducao = translator.translate(anime_dict.get('desc'), dest='pt')

            self.tb_sinopse.setText(traducao.text)
        except:
            self.tb_sinopse.setText(anime_dict.get('desc'))

        self.lbl_nota.setText(str(anime_dict.get('average_score')))

        if os.path.exists('img/' + anime + '.jpg'):
            self.lbl_animage.setPixmap(QtGui.QPixmap(f'img/{anime}.jpg'))
            self.lbl_animage.setScaledContents(True)



    def back_principal(self):
        self.principal = Principal()
        self.hide()
        self.principal.show()


def check_conection():  # check if user is connected on internet
    url = "https://www.google.com"
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except:
        connection_error = QMessageBox()
        connection_error.setWindowIcon(QIcon('img/cross.png'))
        connection_error.setIcon(QMessageBox.Critical)
        connection_error.setMinimumSize(600, 1000)
        connection_error.setText('Falha na conexão, por favor verifique se está conectado a internet')
        connection_error.setWindowTitle('Erro de conexão')
        connection_error.setStandardButtons(QMessageBox.Ok)
        connection_error.setStyleSheet('QMessageBox{color:white;Background-color:Black;} QLabel{color:white;} '
                                       'QPushButton{ '
                                       'Background-color:Transparent;width:50px; color:white; '
                                       'border-radius:30px; Border:1px solid white;} QPushButton:hover{'
                                       'Background:red; Font-Weight:Bold;}')
        connection_error.exec()


class Principal(QMainWindow, Ui_Mw_inicial):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.effect()
        self.information = Information()
        self.Btn_buscar.clicked.connect(self.envia)
        self.setWindowIcon(QIcon('img/esfera.ico'))
        self.setWindowTitle('Busca anime')

    def effect(self):
        if self.lineEdit.text() != "":
            self.lineEdit.setStyleSheet('QPushButton{border-bottom-color: coral;}')

    def envia(self):
        check_conection()
        name = str(self.lineEdit.text())
        anilist = Anilist()
        anime_dict = anilist.get_anime(name)
        self.hide()

        if not os.path.exists('img/' + name + '.jpg'):  # if not have image from anime
            print('não achou antes de abrir a janela')
            self.information.dowload_animage(name, anime_dict.get('cover_image'))
            os.rename(f'{name + ".jpg"}', f'img/{name + ".jpg"}')
            self.information.lbl_animage.setPixmap(QtGui.QPixmap(f'img/{name}.jpg'))
            self.information.lbl_animage.setScaledContents(True)

        self.information.description(name)
        self.information.show()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    principal = Principal()
    principal.show()

    check_conection()
    sys.exit(qt.exec())
