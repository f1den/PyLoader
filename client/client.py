# Импорт библиотек
import sys
import os
import subprocess
import random
from PyQt5 import QtCore, QtGui, QtWidgets
import threading

# Ипрот файла интерфейса
from interface.loader import Ui_Loader
# Импорт прочих обрабртчиков
from handlers.server.server import Server
from handlers.logger.logger import Logger
from handlers.defender.anticrack import prosesses_checker

global reg_menu
reg_menu = False


class Loader(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.loader_ui = Ui_Loader()
        self.loader_ui.setupUi(self)
        self.server = Server()
        self.log = Logger()

        # Получаем hwid
        self.hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
        # Включем чекер процессов
        threading.Thread(target=prosesses_checker, args=(self.hwid,)).start()

        # Скрываем панель регистрации
        self.loader_ui.frame_register.hide()

        # Подключаем кнопки топ бара
        self.loader_ui.button_close.clicked.connect(lambda: os._exit(1))   # Я так и не понял что правильнее loader.close() или sys.exit()
        self.loader_ui.button_hide.clicked.connect(lambda: loader.showMinimized())

        self.loader_ui.button_registration_menu.clicked.connect(self.registration_menu)
        self.loader_ui.button_back.clicked.connect(self.registration_menu)

        # Кнопка входа
        self.loader_ui.button_login.clicked.connect(self.login)

        # Кнопка регистрации
        self.loader_ui.button_registration.clicked.connect(self.registration)

    def login(self):
        username = self.loader_ui.lineEdit_username.text()
        password = self.loader_ui.lineEdit_password.text()

        if username and password:
            message = ['login', username, password, self.hwid]
            self.server.send_message(str(message))

    def registration(self):
        username = self.loader_ui.lineEdit_reg_username.text()
        password = self.loader_ui.lineEdit_reg_password.text()
        key = self.loader_ui.lineEdit_reg_key.text()

        if username and password and key:
            message = ['registration', username, password, self.hwid, key]
            self.server.send_message(str(message))

    def registration_menu(self):
        global reg_menu
        reg_menu = not reg_menu

        if reg_menu:
            self.loader_ui.frame_login.hide()
            self.loader_ui.frame_register.show()
        else:
            self.loader_ui.frame_login.show()
            self.loader_ui.frame_register.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    loader = Loader()

    # Установка рандомного мнени окна.
    _window_title = ''
    for title in range(4, 16):
        _window_title += random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789')
    loader.setWindowTitle(_window_title)

    # Установка WinApi флагов
    loader.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    loader.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    # Проверка процессов
    loader.show()
    sys.exit(app.exec_())
