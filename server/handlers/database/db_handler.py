import sqlite3
import datetime
import random
import os
from handlers.logger.logger import Logger


class Database():
    def __init__(self) -> None:
        self.log = Logger()
        try:
            # Подключение к бд
            self.db = sqlite3.connect('database/database.db', check_same_thread=False)
            self.sql = self.db.cursor()
        except Exception as _error:
            self.log.error(_error)
        finally:
            self.create_tables()

    def create_tables(self):
        # Проверка и создание таблиц в бд
        self.sql.execute("""CREATE TABLE IF NOT EXISTS "users" (
        "id" INTEGER NOT NULL,
        "username" varchar(128) NOT NULL,
        "password" varchar(128) NOT NULL,
        "hwid" TEXT,
        "status" TEXT NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT)
        );
        """)
        self.db.commit()

        self.sql.execute("""CREATE TABLE IF NOT EXISTS "keys" (
            "id" INTEGER NOT NULL,
            "key" TEXT NOT NULL,
            "type" TEXT NOT NULL,
            "status" TEXT NOT NULL,
            "days"	INTEGER NOT NULL,
            "owner"	varchar(128),
            "endtime" TEXT,
            PRIMARY KEY("id" AUTOINCREMENT)
            );
            """)
        self.db.commit()

        self.sql.execute("""CREATE TABLE IF NOT EXISTS "warns" (
            "id" INTEGER NOT NULL,
            "ip" VARCHAR(128) NOT NULL,
            "hwid" VARCHAR(128) NOT NULL,
            "process" VARCHAR(128) NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT)
            );
            """)
        self.db.commit()

        self.sql.execute("""CREATE TABLE IF NOT EXISTS "bans" (
            "id" INTEGER NOT NULL,
            "ip" VARCHAR(128),
            "hwid" VARCHAR(128),
            PRIMARY KEY("id" AUTOINCREMENT)
            );
            """)
        self.db.commit()

    def login(self, ip, username: str, password: str, hwid: str):
        ban_check = self.ban_check(ip, hwid)
        print(ban_check)
        self.sql.execute(f"SELECT username, password, hwid FROM users WHERE username = '{username}'")

        try:
            data_username, data_password, data_hwid = self.sql.fetchone()
        except TypeError:
            return "user not found"
        except Exception as _error:
            self.log.error(_error)


        # Проверяем логин и пароль
        if ban_check == "not banned":
            if data_username == username and data_password == password:
                # Проверяем хвид
                if data_hwid == hwid:
                    self.log.info(f"Пользователь {username} выполнил вход.")
                    return "success"
                elif data_hwid is None:
                    self.sql.execute(f"UPDATE users SET hwid = '{hwid}' WHERE username = '{username}'")
                    self.db.commit()
                    self.log.info(f"У пользователя {username} обновлен hwid на {hwid}")
                    return "success"
                else:
                    self.log.info(f"Попытка авторизации в пользователя {username} с несовподающим hwid!")
                    return "hwid not success"

        elif ban_check == "banned":
            if data_username == username and data_password == password:
                self.sql.execute(f"UPDATE users SET status = ? WHERE username = ?", ('banned', username,))
                self.db.commit()
                return "banned"

    def registration(self, ip, username: str, password: str, hwid: str, key: str):
        self.sql.execute(f"SELECT status, days FROM keys WHERE key = ?", (key,))

        try:
            data_status, data_days = self.sql.fetchone()
        except TypeError:
            return "key not found"
        except Exception as _error:
            self.log.error(_error)

        if data_status != "new":
            return "key is already activated"

        self.sql.execute(f"SELECT username FROM users WHERE username = ?", (username,))
        if self.sql.fetchone() is not None:
            return "user already exists"

        self.sql.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?)", (None, username, password, hwid, "active"))
        self.db.commit()
        self.log.info(f'Создан пользователь {username}.')

        endtime = datetime.datetime.now().date() + datetime.timedelta(days=int(data_days))
        self.sql.execute(f"UPDATE keys SET status = 'use', owner = ?, endtime = ? WHERE key = ?", (username, endtime, key,))
        self.db.commit()
        self.log.info(f"Ключ {key} активирован пользователем {username}.")
        return "registration success"

    def ban_check(self, ip, hwid):
        self.sql.execute(f"SELECT * FROM bans WHERE ip = ? AND hwid = ?", (ip, hwid))
        if self.sql.fetchone() is None:
            return "not banned"
        return "banned"

    def warn(self, ip, hwid, process):
        self.sql.execute(f"INSERT INTO warns VALUES (?, ?, ?, ?)", (None, ip, hwid, process))
        self.db.commit()
        self.log.warn(f"На пк {ip} - {hwid} обнаружен {process}")

        self.sql.execute(f"SELECT count(hwid) FROM warns WHERE hwid = ?", (hwid,))
        warns_count = int(self.sql.fetchone()[0])

        if warns_count >= 10:
            self.sql.execute("SELECT id FROM bans WHERE ip = ? or hwid = ?", (ip, hwid))
            if self.sql.fetchone() is None:
                self.sql.execute("INSERT INTO bans VALUES (?, ?, ?)", (None, ip, hwid))
                self.db.commit()
                self.log.warn(f"Забанен {ip}, {hwid}, количество варнов {warns_count}.")

    def key_gen(self, key_type: str, days: int, count: int):
        chars = '-abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        lenght = 32

        if not os.path.exists('keys'):
            os.mkdir('keys')

        file_name = "Key gen - " + str(datetime.datetime.now().today().replace(microsecond=0)).replace(':', '.')

        for n in range(count):
            key = ''
            for i in range(lenght):
                key += random.choice(chars)

            key = key + "-" + days
            self.sql.execute(f'SELECT key FROM keys WHERE key = ?', (key,))

            if self.sql.fetchone() is None:
                self.sql.execute(f"INSERT INTO keys VALUES (?, ?, ?, ?, ?, ?, ?)", (None, key, key_type, 'new', days, None, None))
                with open(f'keys/{file_name}.txt', 'a') as output:
                    output.write(key + '\n')

        self.db.commit()
        self.log.info(f"Сгенерерировнно {count} {key_type} ключей на {days} дней.")
