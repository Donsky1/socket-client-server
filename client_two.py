from threading import Thread

from client import Client

client2 = Client('Dasha', '', 50003)


def send():
    while True:
        message = input('Сообщение для отправки: ')
        client2.send_message(message, 'localhost', 50004)


p1 = Thread(target=client2.get_message)
p2 = Thread(target=send)

p1.start()
p2.start()

p1.join()
p2.join()

