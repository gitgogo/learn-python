#coding=utf-8
'''网络编程'''

#coding=utf-8
from socket import *
from time import ctime

HOST=''
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
	print 'waiting for connection...'
	tcpCliSock,addr=tcpSerSock.accept()
	print '...conected from ',addr

	while True:
		data=tcpCliSock.recv(BUFSIZ)
		if not data:
			break
		tcpCliSock.send('[%s] %s'%(ctime(),data))
		tcpCliSock.close()
tcpSerSock.close()

#clint
HOST='localhost'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	data=raw_input('> ')
	if not data:
		break
	tcpCliSock.send(data)
	data=tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print data
tcpCliSock.close()


#coding=utf-8
#udp时间戳服务器
from socket import *
from time import ctime

HOST=''
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

udpSerSock=socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
	print 'waiting for message...'
	data,addr=udpSerSock.recvfrom(BUFSIZ)
	udpSerSock.sendto('[%s] %s'%(ctime,data),addr)
	print '...received from and return to: ',addr
udpSerSock.close()

#udp客户端
HOST='localhost'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PROT)

udpCliSock=socket(AF_INET,SOCK_DGRAM)
while True:
	data=raw_input('> ')
	if not data:
		break
	udpCliSock.sendto(data,ADDR)
	data,ADDR=udpCliSock.recvfrom(BUFSIZ)
	if not data:
		break
	print data
udpCliSock.close()

#coding=utf-8
#SocketServer时间戳服务器
from SocketServer import (TCPServer as TCP , StreamRequestHandler as HRS)
from time import ctime

HOST=''
PORT=21567
ADDR=(HOST,PORT)

class MyRequestHandler(SRH):
	def handler(self):
		print '...connected from:',self.client_address
		self.wfile.write('[%s] %s'%(ctime(),self.rfile.readline()))

tcpServ=TCP(ADDR,MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()

#客户端
HOST ='localhost'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

while True:
	tcpCliSock=socket(AF_INET,SOCK_STREAM)
	tcpCliSock.connect(ADDR)
	data=raw_input('> ')
	if not data:
		break
	tcpCliSock.send('%s\r\n'%data)
	data=tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print data.strip()
tcpCliSock.close()

