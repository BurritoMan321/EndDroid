import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8888))
s.sendall('Hello, world')
data = s.recv(1024)
s.close()
print ("Received"), repr(data)
