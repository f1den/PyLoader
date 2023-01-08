import os
import time

from handlers.database.db_handler import *


class Menu():
    def __init__(self) -> None:
        self.db = Database()
        self.main_menu_render()

    def gen_key_menu(self):
        key_types = {'1': 'test', '2': 'beta'}

        self.clear()
        print("--- Генерация ключей ---")
        print("[1] Сгенерировать один ключ.")
        print("[2] Сгенерировать несколько ключей.")
        print("[0] Выйти в меню")

        try:
            select = int(input(">>> "))
        except ValueError:
            print("Для ввода доступны только цифры!")
            time.sleep(1.5)
            self.gen_key_menu()

        if select == 0:
            self.main_menu_render()
        elif select == 1:
            self.clear()
            print('-- Выберите тип ключа --')
            print('[1] test')
            print('[2] beta')
            print('[0] Отмена')

            try:
                select = int(input(">>> "))
            except ValueError:
                print("Для ввода доступны только цифры!")
                time.sleep(1.5)
                self.gen_key_menu()
                self.db.key_gen()

            if select == 0:
                self.gen_key_menu()
            elif select == 1 or select == 2:
                key_type = key_types[str(select)]
                self.clear()
                print("--- Введите срок действия ключа ---")
                print("[0] Отмена")

            else:
                print("Раздел не нейден!")
                time.sleep(1.5)
                self.gen_key_menu()
        else:
            print("Раздел не нейден!")
            time.sleep(1.5)
            self.gen_key_menu()

    def main_menu_render(self):
        self.clear()
        print("--- Основное меню ---")
        print("[1] Генерация ключей.")

        try:
            select = int(input(">>> "))
        except ValueError:
            print("Для ввода доступны только цифры!")
            time.sleep(1.5)
            self.main_menu_render()

        if select == 1:
            self.gen_key_menu()
        else:
            print("Раздел не нейден!")
            time.sleep(1.5)
            self.main_menu_render()

    def clear(self):
        os.system('cls')
