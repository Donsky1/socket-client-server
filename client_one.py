from threading import Thread

from client import Client

client1 = Client('Pasha', '', 50004)


def send():
    while True:
        message = input('Сообщение для отправки: ')
        client1.send_message(message, 'localhost', 50003)


p1 = Thread(target=client1.get_message)
p2 = Thread(target=send)

p1.start()
p2.start()

p1.join()
p2.join()
