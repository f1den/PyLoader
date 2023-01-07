import socket
import os
import time

from handlers.csl_interface.interface import *
from handlers.crypter.crypter import *
from handlers.database.db_handler import *


class Server():
    def __init__(self) -> None:
        # Menu()
        test = Database().registration('firocoreee', '123', '11', 'test')
        print(test)


if __name__ == "__main__":
    Server()
