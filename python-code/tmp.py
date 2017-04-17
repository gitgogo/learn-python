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
passwd='xxxxx'
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