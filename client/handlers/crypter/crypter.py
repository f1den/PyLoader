import cryptocode
import json
from datetime import datetime, timezone

from handlers.logger.logger import Logger


class Crypter():
    def __init__(self) -> None:
        self._log = Logger()

        self._hour = datetime.now(timezone.utc).time().hour
        self._date = datetime.now(timezone.utc).date().day

        self._key = "1q2w3e4r5y"

    def message_encrypt(self, message):
        '''Защифровать сообщение'''
        msc = str(self._hour * self._date) + self._key
        return cryptocode.encrypt(message, msc)

    def message_decrypt(self, message):
        '''Расшифровать сообщение'''
        msc = str(self._hour * self._date) + self._key
        return cryptocode.decrypt(message, msc)
