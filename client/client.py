# Импорт библиотек
import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets
import threading

# Ипрот файла интерфейса
from interface.loader import Ui_Loader
# Импорт прочих обрабртчиков
from handlers.logger.logger import Logger
from handlers.defender.anticrack import posesses_checker

global reg_menu
reg_menu = False


class Loader(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.loader_ui = Ui_Loader()
        self.loader_ui.setupUi(self)
        self.log = Logger()

        # Проверка процессов
        threading.Thread(posesses_checker())

        # Скрываем панель регистрации
        self.loader_ui.frame_register.hide()

        # Подключаем кнопки топ бара
        self.loader_ui.button_close.clicked.connect(lambda: sys.exit())   # Я так и не понял что правильнее loader.close() или sys.exit()
        self.loader_ui.button_hide.clicked.connect(lambda: loader.showMinimized())

        self.loader_ui.button_registration_menu.clicked.connect(self.registration_menu)
        self.loader_ui.button_back.clicked.connect(self.registration_menu)

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

    # Становка WinApi флагов
    loader.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    loader.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    # loader.show()
    sys.exit(app.exec_())
