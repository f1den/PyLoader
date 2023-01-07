import cryptocode
import json
from datetime import datetime, timezone


class Crypter():
    def __init__(self) -> None:
        with open('server/config.json', 'r') as config:
            config = json.load(config)
            print(config)