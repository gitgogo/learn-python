#coding=utf-8
#提示输入字符后，客户端显示服务器返回的带时间戳的字符串
from socket import *
HOST='localhost'
PORT=21567
ADDR=(HOST,PORT)
BUFSIZ=1024

tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	data=raw_input('>>')
	if not data:
		break
	tcpCliSock.send(data)
	data=tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print data
tcpCliSock.close()