import os
import time
from pick import pick

from handlers.database.db_handler import *


class Interface():

    def key_gen(self):
        title = 'Генерация ключей.'
        options = ['Сгенерировать один ключ.', 'Сгенерировать несколько ключей.', 'Выйти в меню']

        selected = pick(options, title, multiselect=False, min_selection_count=0)

        if selected[1] == 0:
            title = 'Выберите тип ключа.'
            options = ['beta', 'test', 'Отмена']

            selected = pick(options, title, multiselect=False, min_selection_count=0)

            if selected[0] == 'Отмена':
                self.key_gen()

            key_type = selected[0]

            title = 'Выберите срок действия ключа'
            options = ['1', '7', '14', '30', '60', '90', '999', 'Отмена']

            selected = pick(options, title, multiselect=False, min_selection_count=0)

            if selected[0] == 'Отмена':
                self.key_gen()

            key_days = selected[0]
            self.db.key_gen(key_type, key_days, 1)
            self.main_menu()

        elif selected[1] == 1:
            title = 'Выберите тип ключей.'
            options = ['beta', 'test', 'Отмена']

            selected = pick(options, title, multiselect=False, min_selection_count=0)

            if selected[0] == 'Отмена':
                self.key_gen()

            key_type = selected[0]

            title = 'Выберите срок действия ключей.'
            options = ['1', '7', '14', '30', '60', '90', '999', 'Отмена']

            selected = pick(options, title, multiselect=False, min_selection_count=0)

            if selected[0] == 'Отмена':
                self.key_gen()

            key_days = selected[0]

            title = 'Выберите количество ключей для генерации.'
            options = ['5', '10', '20', '50', '100', '200', '500', 'Отмена']

            selected = pick(options, title, multiselect=False, min_selection_count=0)

            if selected[0] == 'Отмена':
                self.key_gen()

            key_count = int(selected[0])

            self.db.key_gen(key_type, key_days, key_count)

            self.main_menu()

        elif selected[0] == 'Выйти в меню':
            self.main_menu()

    def main_menu(self):
        self.db = Database()
        title = 'Основное меню.'
        options = ['Генерация ключей', 'Управление пользователями', 'test']

        selected = pick(options, title, multiselect=False, min_selection_count=0)

        if selected[1] == 0:
            self.key_gen()
        elif selected[1] == 1:
            pass
        elif selected[1] == 2:
            pass
