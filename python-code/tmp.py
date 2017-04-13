#coding=utf-8
#服务端接收请求
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9994))
s.listen(5)
print 'Waiting for connection...'

def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        # sock.send('what can I do for you? sir...')
        time.sleep(1)
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        elif 'weather' in data :
            sock.send(handler.show_weather().encode('utf-8'))
        elif 'who' in data:
            sock.send("I'm your friend...Bob")
    sock.close()
    print 'Connection from %s:%s closed.' % addr

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
