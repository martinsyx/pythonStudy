#!/usr/bin/python3

import socket
import sys


server  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('0.0.0.0',8000))
server.listen()
sock,addr = server.accept()
data = sock.recv(1024)
print(data.decode('utf8'))
# sock.send("hello {}".format(data.decode('utf8')))
# sock.send('hello{}'.encode('utf8'))
sock.send('hello {}'.format(data.decode("utf8")).encode('utf8'))
server.close()
sock.close()