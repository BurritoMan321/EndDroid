import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.25.222.125', 8080))
s.sendall(b'Hello, world')
data = s.recv(1024)
s.close()
print ("Received"), repr(data)
