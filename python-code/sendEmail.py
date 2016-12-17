#coding=utf-8
'''
发送邮件给多人
'''
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
	message['To']=receiver
	message['Cc']=''#抄送
	message['Bcc']=''#密送

	mail_body='''
hello,all
	This is a test mail by myself from python.
	'''
	message.attach(MIMEMultipart(mail_body,'plain','utf-8'))
	#添加附件
	attach_filepath='./aa.txt'
	attach_file=open(attach_filepath,'rb')
	attach_part=MIMEApplication(attach_file.read(),Name=os.path.basename(attach_filepath))
	attach_part['Content-Disposition']='attachment: filename=%s'%os.path.basename(attach_filepath)
	attach_file.close()
	message.attach(attach_part)

	try:
		smtp=smtplib.SMTP_SSL()
		smtp.connect(smtp_server)
		smtp.login(sender,sender_pwd)
		smtp.sendmail(sender,receiver,message.as_string())
		smtp.close()
		print 'done!!'
	except Exception,e:
		print e

main()
# if __name__=='__mail__':
# 	main()


