#coding=utf-8
'''
发送邮件给多人
'''
##############HTML格式的邮件################
import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def main():
	sender='ldjwyyx@163.com'
	sender_pwd='wy1989-10-26'
	smtp_server='smtp.163.com'
	receiver=['865479851@qq.com','liudongjie2015@126.com']

	message=MIMEMultipart()
	message['Subject']='test email by python'
	message['From']=sender
	message['To']=','.join(receiver)
	# message['Cc']=''#抄送
	# message['Bcc']=''#密送

	mail_body='''
	<h1>header</h1>
	<h1>测试邮件</h1>
    <h2 style="color:red">This is a test</h2>
	<p>This is a test mail by myself from python.</p>
	'''
	message.attach(MIMEText(mail_body,'html','utf-8'))
	#纯文本内容
	# message=MIMEText(mail_body,'plain','utf-8')
	#添加附件
	attach_filepath='aa.txt'
	attach_file=open(attach_filepath,'rb')
	attach_part=MIMEApplication(attach_file.read(),Name=os.path.basename(attach_filepath))
	attach_part['Content-Disposition']='attachment: filename=%s'%os.path.basename(attach_filepath)
	attach_file.close()
	message.attach(attach_part)

	try:
		# smtp=smtplib.SMTP_SSL()
		smtp=smtplib.SMTP()
		smtp.connect(smtp_server)
		smtp.login(sender,sender_pwd)
		smtp.sendmail(sender,receiver,message.as_string())
		smtp.close()
		print 'done!!'
	except Exception,e:
		print e

if __name__=='__main__':
	main()


#####################带附件的邮件########################
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
# 格式化邮件地址
def formatAddr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
def sendMail(body, attachment):
    smtp_server = 'smtp.163.com'
    from_mail = 'ldjwyyx@163.com'
    mail_pass = 'wy1989-10-26'
    to_mail = ['865479851@qq.com', 'xxx@163.com']
    # 构造一个MIMEMultipart对象代表邮件本身
    msg = MIMEMultipart()
    # Header对中文进行转码
    msg['From'] = formatAddr('管理员 <%s>' % from_mail).encode()
    msg['To'] = ','.join(to_mail)
    msg['Subject'] = Header('监控', 'utf-8').encode()
    # plain代表纯文本
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    # 二进制方式模式文件
    with open(attachment, 'rb') as f:
        # MIMEBase表示附件的对象
        mime = MIMEBase('text', 'txt', filename=attachment)
        # filename是显示附件名字
        mime.add_header('Content-Disposition', 'attachment', filename=attachment)
        # 获取附件内容
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        # 作为附件添加到邮件
        msg.attach(mime)
    try:
        s = smtplib.SMTP()
        s.connect(smtp_server, "25")
        s.login(from_mail, mail_pass)
        s.sendmail(from_mail, to_mail, msg.as_string())  # as_string()把MIMEText对象变成str
        s.quit()
    except smtplib.SMTPException as e:
        print "Error: %s" % e
if __name__ == "__main__":
    sendMail('附件是测试数据, 请查收！', 'test.txt')

############带图片的邮件#############
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr
# 格式化邮件地址
def formatAddr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
def sendMail(body, image):
    smtp_server = 'smtp.163.com'
    from_mail = 'baojingtongzhi@163.com'
    mail_pass = 'xxx'
    to_mail = ['xxx@qq.com', 'xxx@163.com']
    # 构造一个MIMEMultipart对象代表邮件本身
    msg = MIMEMultipart() 
    # Header对中文进行转码
    msg['From'] = formatAddr('管理员 <%s>' % from_mail).encode()
    msg['To'] = ','.join(to_mail)
    msg['Subject'] = Header('监控', 'utf-8').encode()
    msg.attach(MIMEText(body, 'html', 'utf-8'))
    # 二进制模式读取图片
    with open(image, 'rb') as f:
        msgImage = MIMEImage(f.read())
    # 定义图片ID
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)
    try:
        s = smtplib.SMTP()     
        s.connect(smtp_server, "25")   
        s.login(from_mail, mail_pass)
        s.sendmail(from_mail, to_mail, msg.as_string())  # as_string()把MIMEText对象变成str     
        s.quit()
    except smtplib.SMTPException as e:
        print "Error: %s" % e
if __name__ == "__main__":
    body = """
    <h1>测试图片</h1>
    <img src="cid:image1"/>    # 引用图片
    """
    sendMail(body, 'test.png')
