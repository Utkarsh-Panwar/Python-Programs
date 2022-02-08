# -*- coding: utf-8 -*-
import socket
 
TCP_IP = '127.0.0.1'
TCP_PORT = 62
BUFFER_SIZE = 1024
MESSAGE = "Hello from client!"
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(bytes(MESSAGE,'utf8'))
data = s.recv(BUFFER_SIZE)
s.close()
 
print("received data:", data)