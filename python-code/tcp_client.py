#coding=utf-8
#udp客户端
import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#不需要建立连接connection，sendto需传入发送的数据+地址
for name in ['bob','jack','lucy']:
	client.sendto(name,('127.0.0.1',8888))
	print client.recv(1024)
client.close()