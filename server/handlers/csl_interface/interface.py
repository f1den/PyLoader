import os
import time


class Menu():
    def __init__(self) -> None:
        self.main_menu_render()

    def gen_key_menu(self):
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
