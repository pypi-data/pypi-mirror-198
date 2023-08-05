"""
:authors: v.oficerov
:license: MIT License
:copyright: (c) 2023 v.oficerov
"""

import logging
import socket
import traceback
from http.client import HTTPConnection
from json import dumps


class HTTPHandler(logging.Handler):
    """Хендлер для отправки логов в graylog посредством http протокола"""

    def __init__(self, host: str, port: int = None, timeout: int = 10, path: str = '/gelf',
                 machine: str = socket.gethostname()):
        super().__init__()
        self._machine: str = machine
        self._path = path
        self._additional_fields = dict()
        self._headers = {"Content-type": "application/json", "Accept": "application/json", "charset": "utf-8"}
        self._connection = HTTPConnection(host=f"{host}:{port}", timeout=timeout)
        self.response = None

    def __del__(self):
        if self.__getattribute__('_connection'):
            self._connection.close()

    def _level(self, level: str):
        match level:
            case 'DEBUG':
                self.level = 7
            case 'INFO':
                self.level = 6
            case 'WARNING':
                self.level = 4
            case 'ERROR':
                self.level = 3
            case 'CRITICAL':
                self.level = 2

    def _prepare_exceptions(self, record: logging.LogRecord):
        if record.exc_info is not None:
            self._additional_fields.update({'traceback': traceback.format_exc()})

    def add_field(self, name: str, content: str):
        """Добавляет кастомное поле"""
        self._additional_fields.update({name: content})
        return self

    def emit(self, record):
        """Отправляет сообщение в graylog"""
        self._level(level=record.levelname)
        self._prepare_exceptions(record=record)
        body = dumps({'version': '1.1',
                      'host': self._machine,
                      'message': str(record.msg),
                      'level': self.level,
                      'logger_name': record.name,
                      } | self._additional_fields)
        self._connection.request("POST", self._path, body, self._headers)
        self.response = self._connection.getresponse()
