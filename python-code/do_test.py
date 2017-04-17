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

#服务端接收请求UDP
import socket
udpServer=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpServer.bind(('127.0.0.1',8888))
print 'bind udp on 8888...' #udp不需要listen，接收方法返回数据+地址，recvfrom，发送消息sendto
while True:
    data,addr=udpServer.recvfrom(1024)
    udpServer.sendto('hello,%s'%data,addr)

#udp客户端
import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#不需要建立连接connection，sendto需传入发送的数据+地址
for name in ['bob','jack','lucy']:
    client.sendto(name,('127.0.0.1',8888))
    print client.recv(1024)
client.close()

#电子邮件📧
import smtplib
from email.mime.text import MIMEText

msg=MIMEText('send from your friend by python...','palin','utf-8')

from_addr='ldjwyyx@163.com'
passwd='wy1989-10-26'
send_to='865479851@qq.com'
smtp_server='smtp.163.com'
msg['From']=from_addr
msg['Subject']='xxx'
msg['To']=send_to
server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,passwd)
server.sendmail(from_addr,[send_to],str(msg))
#554 DT:SPM 发送的邮件内容包含了未被许可的信息，或被系统识别为垃圾邮件。
# 请检查是否有用户发送病毒或者垃圾邮件
server.quit()

#添加附件的邮件
#coding=utf-8
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),
        addr.encode('utf-8') if isinstance(addr,unicode) else addr))

from_addr='ldjwyyx@163.com'
passwd='wy1989-10-26'
to_addr='865479851@qq.com'
smtp_server='smtp.163.com'

body='''
<html>
    <body>
        <h1>Hello</h1>
        <p>send by <a href="http://www.python.org">Python</a>...</p>
        <p><img src="cid:0"></p>  <!-- 将附件的图片添加至正文显示 -->
    </body></html>
'''
msg=MIMEMultipart('alternative')
#同事支持HTML和plain格式，由于部分古老设备不支持HTML，则可以选择接收plain格式
msg.attach(MIMEText('hello this is your info...','plain','utf-8'))
#添加正文部分
msg.attach(MIMEText(body,'html','utf-8')) 
msg['From']=_format_addr(u'大哥<%s>'%from_addr)
msg['To']=_format_addr(u'小弟<%s>'%to_addr)
msg['Subject']=Header(u'来自SMTP的问候。。。','utf-8').encode()
#发送附件
with open('/Users/ralphliu/Desktop/1.png','rb') as f:
    mime=MIMEBase('image','png',filename='1.png')
    mime.add_header('Content-Disposition','attachment',filename='1.png')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime) #添加附件

server=smtplib.SMTP(smtp_server,25)
server.starttls() #加密传输，如Gmail的SMTP是587，使用加密传输
server.set_debuglevel(1)
server.login(from_addr,passwd)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

#pop收取电子邮件
# -*- coding: utf-8 -*-

import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

email = 'liudongjie2015@126.com'
password = 'liudongjie126'
pop3_server = 'pop.126.com'

server = poplib.POP3(pop3_server)
#server.set_debuglevel(1)
print(server.getwelcome())
# 认证:
server.user(email)
server.pass_(password)
print('Messages: %s. Size: %s' % server.stat())
resp, mails, octets = server.list()
# 获取最新一封邮件, 注意索引号从1开始:
resp, lines, octets = server.retr(len(mails))
# 解析邮件:
msg = Parser().parsestr('\r\n'.join(lines))
# 打印邮件内容:
print_info(msg)
# 慎重:将直接从服务器删除邮件:
# server.dele(len(mails))
# 关闭连接:
server.quit()

#mysqlalchemy
#coding=utf-8
#step1 导入SQLalchemy，并且初始化
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class User(Base):
    __tablename__='user'
    id=Column(String(20),primary_key=True)
    name=Column(String(20))

#数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名
engine=create_engine('mysql+mysqldb://root:root@localhost:3306/tmp')
DBSession=sessionmaker(bind=engine)
#创建session对象
session=DBSession()
new_user=User(id='5',name='bob')
# session.add(new_user)
# session.commit()

user=session.query(User).filter(User.id=='5').one()
print 'type:',type(user)
print 'name:',user.name
session.close()

#一对多联表查询
class User(Base):
    __tablename__='user':
    id=Column(String(20),primary_key=True)
    name=Column(String(20))
    books=relationship('Book')

class Book(Base):
    __tablename__='book'
    id=Column(String(20),primary_key=True)
    name=Column(String(20))
    user_id=Column(String(20),ForeignKey('user.id'))

#web开发
#coding=utf-8
def application(environ,start_response):
    start_response('200 ok',[('Content-Type','text/html')])
    return '<h1>Hello, %s</h1>'%(environ['PATH_INFO'][1:] or 'web')

from wsgiref.simple_server import make_server

httpd=make_server('',8000,application)
print 'Serving HTTP on port 8000'
httpd.serve_forever()

#Flask框架
#coding=utf-8
from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form> '''

@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username']=='admin' and request.form['password']=='1234':
        return '<h3>Hello, admin</h3>'
    return '<h3>Bad username or password</h3>'

if __name__ == '__main__':
    app.run()

# 使用MVC模型进行web开发
#coding=utf-8
from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
    username=request.form['username']
    password=request.form['password']
    if username=='admin' and password=='1234':
        return render_template('signin_ok.html',username=username)
    return render_template('form.html',message='bad username or password',username=username)

if __name__ == '__main__':
    app.run()