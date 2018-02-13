#!/usr/bin/python3

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)

try:
    while True:
        numero = random.randint(1, 100000000)
        url = "http://localhost:1234/" + str(numero)

        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()

        print('Request received:')
        print(recvSocket.recv(2048))

        recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                        b"<html><body><h1>Hello!!</h1>" + 
                        bytes('<a href=' + url + '>Dame otra</a>\r\n', 'utf-8') +
                        b"</body></html>" +
                        b"\r\n")
        recvSocket.close()
        
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
