from threading import Thread

from client import Client

client2 = Client('Dasha', '', 50003)


p1 = Thread(target=client2.get_message)
p2 = Thread(target=client2.send_message, args=('localhost', 50004))

p1.start()
p2.start()


