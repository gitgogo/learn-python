#coding=utf-8
#date:2017-04-10
try:
    import cPickle as pickle
except ImportError:
    import pickle

d=dict.fromkeys(list('ralph'),4) #字典的fromkeys方法
l=list('beijing')
# print pickle.dumps(d)
with open('12.txt','wb') as f:
    pickle.dump(d,f)

with open('12.txt') as f:
    d1= pickle.load(f)
    assert d1==d

import json #json序列化
print json.dumps(d)
with open('12.txt','wb') as f:
    json.dump(d,f)
    # json.dump(l,f) #不可对非字典对象dump 

with open('12.txt') as f:
    print json.load(f)

class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

    def study(self):
        print 'i am studying'

xm=Student('xm',78,99.5)
print json.dumps(xm,default=lambda x:x.__dict__)

def dict2obj(dict_str):
    return Student(dict_str['name'],dict_str['age'],dict_str['score'])

dict_str='{"name":"jack","age":33,"score":89.9}'
jack=json.loads(dict_str,object_hook=dict2obj)
print "jack's name is ",jack.name
jack.study()

#base64 module
import base64
print base64.b64encode('abcd')
print base64.b64decode('aGVsbG8xMjM=')
print base64.urlsafe_b64encode('&hhkl') #url safe
print base64.urlsafe_b64decode('aGVsbG8xMjM=')
#可处理去掉=的base64解码函数
def safe_b64decode(code):
 length=len(code)
 if length%4:
  code=code+'='*(4-length%4)
  return base64.b64decode(code)
 else:
  return base64.b64decode(code)
print safe_b64decode('YWJjZA')

#python xml module
#coding=utf-8
# ['dom', 'parsers', 'sax', 'etree']
import urllib
from xml.parsers.expat import ParserCreate
import re
# 解析天气预报,百度天气
xml = ''
url='http://api.map.baidu.com/telematics/v2/weather?location=%E5%8C%97%E4%BA%AC&ak=B8aced94da0b345579f481a1294c9094'
try:
    page = urllib.urlopen(url)
    xml = page.read()
finally:
    page.close()
# print xml
class BaiduWeatherSaxHandler(object):
    def __init__(self):
        self._weather = dict()
        self._count = 0
        self._current_element = ''
    def start_element(self, name, attrs):
        if name == 'result':
            self._count += 1
            self._weather[self._count] = dict()
        self._current_element = name
    def end_element(self, name):
        pass
    def char_data(self, text):
        # 排除换行符和空白内容
        re_str = '^[\n|\s]+$'
        if self._current_element and not re.match(re_str, text) and self._weather:
            self._weather[self._count][self._current_element] = text
    def show_weather(self):
        for v in self._weather.values():
            print v['date'], '\t'*(7-len(v['date'])), v['temperature'], v['weather'], v['wind']
handler = BaiduWeatherSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
handler.show_weather()

#Python HTMLParser模块
#解析Python官网发布的Python会议，输出内容
from HTMLParser import HTMLParser
import urllib

class PyEventParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self._count = 0
        self._events = dict()
        self._flag = None

    def handle_starttag(self, tag, attrs):
        if tag == 'h3' and attrs.__contains__(('class', 'event-title')):
            self._count += 1
            self._events[self._count] = dict()
            self._flag = 'event-title'
        if tag == 'time':
            self._flag = 'time'
        if tag == 'span' and attrs.__contains__(('class', 'event-location')):
            self._flag = 'event-location'

    def handle_data(self, data):
        # if self._flag == 'event-title':
        #     self._events[self._count][self._flag] = data
        # if self._flag == 'time':
        #     self._events[self._count][self._flag] = data
        # if self._flag == 'event-location':
        #     self._events[self._count][self._flag] = data
        if self._flag:
            self._events[self._count][self._flag]=data
        self._flag = None

    def event_list(self):
        print '近期关于Python的会议有：', self._count, '个，具体如下：'
        for event in self._events.values():
            print event['event-title'], '\t', event['time'], '\t', event['event-location']

try:
    parser = PyEventParser()
    pypage = urllib.urlopen('https://www.python.org/events/python-events/')
    pyhtml = pypage.read()
except IOError,e:
    print 'IOError:', e
else:
    parser.feed(pyhtml)
    parser.event_list()
finally:
    pypage.close()

#python GUI编程
from Tkinter import *
import tkMessageBox
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput=Entry(self)
        # self.helloLabel = Label(self, text='Hello, world!')
        # self.helloLabel.pack()
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
        self.button=Button(self,text='Quit',command=self.quit)
        self.button.pack()

    def hello(self):
        name=self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message','Hello %s' %name)

app=Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()

#TCP编程，客户端请求
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.qq.com',80))
s.send('GET / HTTP/1.1\r\nHost: www.qq.com\r\nConnection: close\r\n\r\n')
#接收数据
buff=[]
while True:
    d=s.recv(1024)
    if d:
        buff.append(d)
    else:break
data=''.join(buff)
s.close()

header,html=data.split('\r\n\r\n',1)
print header
with open('qq.html','wb') as f:
    f.write(data)

import socket
import threading
import time
#服务端，接受请求
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5) #max connection 5
print 'waiting for connection...'

def tcpLink(sock,addr):
    print 'Accept connection from %s:%s...'%addr
    s.send('Hello')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if data=='exit' or not data:
            break
        sock.send('Hello ',data)
    sock.close()
    print 'connection from %s:%s closed... '%addr

while True:
    sock,addr=s.accept()
    t=threading.Thread(target=tcpLink,args=(sock,addr))
    t.start()

#客户端，发起请求
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print s.recv(1024)
for name in ['jack','bob','ralph','mike']:
    s.send(name)
    print s.recv(1024) 
s.send('exit')
s.close()

'''
一个完整的智能机器聊天程序，基于tcp网络编程
'''
import socket
import threading
import time
import urllib
from xml.parsers.expat import ParserCreate
import re
# 解析天气预报,百度天气
xml = ''
url='http://api.map.baidu.com/telematics/v2/weather?location=%E5%8C%97%E4%BA%AC&ak=B8aced94da0b345579f481a1294c9094'
try:
    page = urllib.urlopen(url)
    xml = page.read()
finally:
    page.close()
# print xml
class BaiduWeatherSaxHandler(object):
    def __init__(self):
        self._weather = dict()
        self._count = 0
        self._current_element = ''
    def start_element(self, name, attrs):
        if name == 'result':
            self._count += 1
            self._weather[self._count] = dict()
        self._current_element = name
    def end_element(self, name):
        pass
    def char_data(self, text):
        # 排除换行符和空白内容
        re_str = '^[\n|\s]+$'
        if self._current_element and not re.match(re_str, text) and self._weather:
            self._weather[self._count][self._current_element] = text
    def show_weather(self):
        for v in self._weather.values():
            return '%s\t%s\t%s\t%s' %(v['date'], v['temperature'], v['weather'], v['wind'])
handler = BaiduWeatherSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
# print handler.show_weather().encode('utf-8')
# handler.show_weather()

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

#客户端发起询问
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9994))
# 接收欢迎消息:
print s.recv(1024)
while True:
    print 'what can I do for you? sir...'
    # 发送数据:
    data=raw_input('>>') #接收用户输入，如：who、weather，等待服务端响应
    s.send(data)
    print s.recv(1024)
    if data=='exit':
        break
s.send('exit')
s.close()