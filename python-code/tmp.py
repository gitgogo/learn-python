#coding=utf-8
from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR='smtp.163.com'
POP3SVR='pop.163.com'

origHdrs=['From: ldjwyyx@163.com','To: ldjwyyx@163.com','Subject: test msg']
origBody=['xxx','yyy','helloworld']
oriMsg='\r\n\r\n'.join(['\r\n'.join(origHdrs),'\r\n'.join(origBody)])

sendSvr=SMTP(SMTPSVR)
errs=sendSvr.sendmail('ldjwyyx@163.com','ldjwyyx@163.com',oriMsg)
sendSvr.quit()
assert len(errs)==0,errs
sleep(10)

recvSvr=POP3(POP3SVR)
recvSvr.user('ldjwyyx')
recvSvr.pass_('123456')
rsp,msg,siz=recvSvr.retr(recvSvr.stat()[0])

sep=msg.index('')
recvBody=msg[sep+1]
assert origBody==recvBody