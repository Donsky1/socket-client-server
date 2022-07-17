import socket
from config import HOST, PORT, BUFFER

with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print(f'Соединение установлено с {addr}')
        while True:
            data = conn.recv(BUFFER)
            if not data: break
            conn.sendall(data.upper())