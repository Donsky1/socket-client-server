import socket
from config import *


class Client:

    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        self.port = port

    @staticmethod
    def send_message(host, port):
        while True:
            message = input('Сообщение для отправки: ')
            with socket.socket() as s:
                s.connect((host, port))
                s.send(bytes(message, 'utf-8'))

    def get_message(self):
        with socket.socket() as s:
            s.bind((self.host, self.port))
            while True:
                s.listen()
                conn, addr = s.accept()
                with conn:
                    while True:
                        data = conn.recv(BUFFER)
                        if not data:
                            break
                        print(f'Пользователь {addr}, сообщение: {data.decode()}')
