#coding=utf-8
#创建一个TCP服务器，把客户端发送过来的字符串加上一个时间戳返回给客户端
from socket import *
from time import ctime

HOST=''
PORT=21567
ADDR=(HOST,PORT)
BUFSIZE=1024

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)#最多允许5个同时连接

while True:
	print 'waiting for connection...'
	tcpCliSock,addr =tcpSerSock.accept()
	print '...connected from:',addr
	while True:
		data=tcpCliSock.recv(BUFSIZE)
		if not data:
			break
		tcpCliSock.send('[%s] %s'%(ctime(),data))
		tcpCliSock.close()
tcpSerSock.close()#程序不会跳出循环，这条语句不会被执行，只是提醒在退出服务器时要调用close()方法