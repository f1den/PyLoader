import socket
import ast
import threading

from handlers.csl_interface.interface import *
from handlers.crypter.crypter import *
from handlers.database.db_handler import *
from handlers.logger.logger import *


class Server():
    def __init__(self) -> None:
        self.crypter = Crypter()
        self.db = Database()
        self.log = Logger()
        self.dis = Discord()
        self.interface = Interface()

        with open('config/config.json', 'r') as config:
            config = json.load(config)
            ip = config['server']['ip']
            port = config['server']['port']

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((ip, port))
        self.server.listen()

        threading.Thread(target=self.listen_connections).start()
        # threading.Thread(target=self.interface.main_menu()).start()

    def client_socket_listener(self, client, addres):
        self.clients.append(client)
        print(self.clients)

        while True:
            try:
                ip = addres[0]
                request = client.recv(2048).decode()
                message = self.crypter.message_decrypt(request)

                if request and message.startswith('[') and message.endswith(']'):
                    message_list = ast.literal_eval(message)
                    message_code = message_list[0]
                    # print(message_code)

                    if message_code == 'login':
                        username = message_list[1]
                        password = message_list[2]
                        hwid = message_list[3]

                        login = self.db.login(ip, username, password, hwid)

                        server_message = ['login', login]
                        server_message = self.crypter.message_encrypt(str(server_message))
                        client.send(server_message.encode())

                    elif message_code == 'registration':
                        username = message_list[1]
                        password = message_list[2]
                        hwid = message_list[3]
                        key = message_list[4]

                        registration = self.db.registration(ip, username, password, hwid, key)

                        server_message = ['registration', registration]
                        server_message = self.crypter.message_encrypt(str(server_message))
                        client.send(server_message.encode())

                    elif message_code == 'warn':
                        ip = str(addres[0])
                        hwid = str(message_list[1])
                        process = str(message_list[2])

                        self.db.warn(ip, hwid, process)
                        # Ответ сервера
                        server_message = ['denied']
                        server_message = self.crypter.message_encrypt(str(server_message))
                        client.send(server_message.encode())
                        break

                else:
                    # Ответ сервера
                    server_message = ['denied']
                    server_message = self.crypter.message_encrypt(str(server_message))
                    client.send(server_message.encode())
                    break

            except Exception as _error:
                self.log.info(_error)
                self.clients.remove(client)
                break

    def listen_connections(self):
        self.clients = []
        self.log.info('Серевер запущен.')
        self.dis.log('Серевер запущен.')
        while True:
            client_socket, client_addres = self.server.accept()
            threading.Thread(target=self.client_socket_listener, args=(client_socket, client_addres)).start()
            self.dis.log(f'Новое подключение из {client_addres}')
            self.log.info(f'Новое подключение из {client_addres}')


if __name__ == "__main__":
    Server()
