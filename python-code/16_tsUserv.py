#coding=utf-8
#创建一个UDP服务器，返回给客户端加了时间戳的字符串
from socket import *
from time import ctime

HOST=''
PORT=21567
ADDR=(HOST,PORT)
BUFSIZ=1024

udpSerSock=socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)
while True:
	print 'waiting for message...'
	data,addr=udpSerSock.recvfrom(BUFSIZ)
	udpSerSock.sendto('[%s] %s'%(ctime(),data),addr)
	print '...received from and returned to:',addr
udpSerSock.close()