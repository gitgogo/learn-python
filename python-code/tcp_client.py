#coding=utf-8
import socket
#客户端，发起请求
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('127.0.0.1',9999))
# print s.recv(1024)
# for name in ['jack','bob','ralph','mike']:
#     s.send(name)
#     print s.recv(1024) 
# s.send('exit')
# s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9994))
# 接收欢迎消息:
print s.recv(1024)
while True:
	print 'what can I do for you? sir...'
    # 发送数据:
	data=raw_input('>>')
	s.send(data)
	print s.recv(1024)
	if data=='exit':
		break
s.send('exit')
s.close()