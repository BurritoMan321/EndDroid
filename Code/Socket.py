import socket
host = '10.25.222.125'
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
while 1:
    data = conn.recv(1024)
    print(data)
    if not data:
        break
    conn.sendall(data)
conn.close()
