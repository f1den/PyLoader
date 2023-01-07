from ctypes.wintypes import *
import ctypes
import os
import sys
import time

from handlers.defender.prohibited_processes import processes_names
from handlers.logger.logger import Logger
from handlers.server.server import Server

PROCESS_ALL_ACCESS = 0x001F0FFF


def list_processes_names() -> list:
    """Возвращает список имен всех активных процессов."""

    quantity = 32
    processes_ids_list = []
    while True:
        process_ids = (DWORD * quantity)()
        quantity_buffer = ctypes.sizeof(process_ids)
        bytes_returned = DWORD()
        if ctypes.windll.Psapi.EnumProcesses(ctypes.byref(process_ids), quantity_buffer, ctypes.byref(bytes_returned)):
            if bytes_returned.value < quantity_buffer:
                processes_ids_list = list(set(process_ids))
                break
            else:
                quantity *= 2

    processes_names = []
    for process_id in processes_ids_list:
        image_file_name = (ctypes.c_char * MAX_PATH)()
        process_handle = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, process_id)
        if ctypes.windll.psapi.GetProcessImageFileNameA(process_handle, image_file_name, MAX_PATH) > 0:
            filename = os.path.basename(image_file_name.value).decode()
            processes_names.append(filename)

    return processes_names


def prosesses_checker():
    log = Logger()

    while True:
        list_processes = list_processes_names()
        for process in processes_names:
            if process in list_processes:
                print(f"Найден процесс {process}!")

                # Отсылание лога о нарушении на сервер!

                # Создание слиент лога
                log.warn(f"Обнаружен процесс {process}! Закройте его, и повторите попытку.")

                os._exit(1)
