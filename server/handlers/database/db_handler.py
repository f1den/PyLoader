import sqlite3
import datetime
from handlers.logger.logger import Logger


class Database():
    def __init__(self) -> None:
        self.log = Logger()
        try:
            # Подключение к бд
            self.db = sqlite3.connect('database/database.db', check_same_thread=False)
            self.sql = self.db.cursor()
            self.log.info("База данных подключена.")
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

    def login(self, username: str, password: str, hwid: str):
        self.sql.execute(f"SELECT username, password, hwid FROM users WHERE username = '{username}'")

        try:
            data_username, data_password, data_hwid = self.sql.fetchone()
        except TypeError:
            return None
        except Exception as _error:
            self.log.error(_error)

        # Проверяем логин и пароль
        if data_username == username and data_password == data_password:
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

    def registration(self, username: str, password: str, hwid: str, key: str):
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
