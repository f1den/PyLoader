import socket
import ast
import os

from handlers.crypter.crypter import Crypter
from handlers.logger.logger import Logger


class Server():
    def __init__(self) -> None:
        self.crypter = Crypter()
        self.log = Logger()
        self._server_connection()

    def _server_connection(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(('localhost', 1337))
            self.log.info("Подключение к серверу установленно.")
        except ConnectionRefusedError:
            self.log.error("Сервер не доступен!")
            os._exit(1)

    def send_message(self, message):
        cmessage = self.crypter.message_encrypt(message)
        self.client.send(cmessage.encode())

        while True:
            response = self.client.recv(2048).decode()
            server_message = self.crypter.message_decrypt(response)
            # print(server_message)

            if server_message and server_message.startswith('[') and server_message.endswith(']'):
                message_list = ast.literal_eval(server_message)
                message_code = message_list[0]
                print(message_code)

                if message_code == "registration" or message_code == "login":
                    return message_list[1]
                elif message_code == "denied":
                    os._exit(1)
