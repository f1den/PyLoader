import cryptocode
import json
from datetime import datetime, timezone

from handlers.logger.logger import Logger


class Crypter():
    def __init__(self) -> None:
        self._log = Logger()

        self._hour = datetime.now(timezone.utc).time().hour
        self._date = datetime.now(timezone.utc).date().day
        try:
            with open('config/config.json', 'r') as config:
                config = json.load(config)
                self._key = config['crypter']['key']
        except Exception as _error:
            self._log.error(_error)

    def message_encrypt(self, message):
        msc = str(self._hour * self._date) + self._key
        return cryptocode.encrypt(message, msc)

    def message_decrypt(self, message):
        msc = str(self._hour * self._date) + self._key
        return cryptocode.decrypt(message, msc)
