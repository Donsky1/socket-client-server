import socket
from config import HOST, PORT, BUFFER

with socket.socket() as s:
    s.connect((HOST, PORT))
    s.sendall(b'pasha')
    data = s.recv(BUFFER)

print('Получено сообщение: ', repr(data))