#Python has built-in support for TCP sockets
#data.pr4e.org - is the HOST
#80 - is the port

#HTTP - HyperText Transfer Protocol
#It is a set of rules that allows browsers to retrieve web documents
#from the servers over the Internet

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
