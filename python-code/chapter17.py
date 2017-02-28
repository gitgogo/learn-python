#coding=utf-8
import ftplib
import os
import socket

HOST='ftp.mozilla.org'
DIRN='pub/mozilla.org/webtools'
FILE='bugzilla-LATEST.tar.gz'

def main():
	try:
		f=ftplib.FTP(HOST)
	except (socket.error,socket.gaierror),e:
		print 'error:cannot reach "%s"'%HOST
		return

	try:
		f.login()
	except ftplib.error_perm:
		print 'error: cannot login anonymously'
		f.quit()
		return
	print '----logged in as "anonymous"'

	try:
		f.cwd(DIRN)
	except ftplib.error_perm:
		print 'error: cannot cd to "%s"'%DIRN
		f.quit()
		return

	try:
		f.retrbinary('RETR %s' %FILE,open(FILE,'wb').write)
	except ftplib.error_perm:
		print 'error: cannot read file %s'%FILE
		os.unlink(FILE)
	else:
		print '---Download %s to CWD'%FILE
	f.quit()
	return

if __name__=='__main__':
	main()

#NNTP新闻组
import nntplib
import socket

HOST='your.nntp.server'
GRNM='comp.lang.python'
USER='ralph'
PASS='itspwd.'

def main():
	try:
		n=nntplib.NNTP(HOST)
		#user=USER,pwd=PASS
	except socket.gaierror,e:
		print 'error,can not reach host',HOST
		return
	except nntplib.NNTPPermanentError,e:
		print 'error,access denied on ',HOST
		return

	try:
		rsp,ct,fst,lst,grp=n.group(GRNM)
	except nntplib.NNTPTemporaryError,e:
		print 'error: cannot load group',GRNM
		print str(e)
		print 'server may require authentication'
		print 'Uncomment/edit login line above'
		n.quit()
		return
	except nntplib.NNTPTemporaryError,e:
		print 'error:group %s unavailable'%GRNM
		print str(e)
		n.quit()
		return
	print '***found newsgroup %s',%GRNM

		rng='%s-%s'%(lst,lst)
		rsp,frm=n.xhdr('from',rng)
		rsp,sub=n.xhdr('subject',rng)
		rsp,dat=n.xhdr('date',rng)
		print '''found last article (#%s):
		from:%s
		subject:%s
		date:%s
		'''%(lst,frm[0][1],sub[0][1],dat[0][1])
		rsp,anum,mid,data=n.body(lst)
		displayFirst20(data)
		n.quit()

def displayFirst20(data):
	print '***First (<20) meaningful lines:\n'
	count=0
	lines=(line.rstrip() for line in data)
	lastBlank=True
	for line in lines:
		if line:
			lower=line.lower()
			if (lower.startswith('>') and not lower.startswith('>>>')) or lower.startswith('|') or lower.startswith(
				'in article') or lower.endswith('writes: ') or lower.endswith('wrote: '):
				continue
		if not lastBlank or (lastBlank and line):
			print '%s'%line
			if line:
				count+=1
				lastBlank=False
			else:
				lastBlank=True
		if count==20:
			break

if __name__ == '__main__':
	main()

#selenium python 模块化
from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest ,time

class login(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url='https://www.baidu.com'
		self.verificationErrors=[]
		self.accept_next_alert=True

	def test_login(self):
		driver=self.driver
		driver.get(self.base_url)
		driver.maximize_window()
		driver.find_element_by_id('user_name').clear()
		driver.find_element_by_id('user_name').send_keys('username')
		driver.find_element_by_id('user_pwd').clear()
		driver.find_element_by_id('user_pwd').send_keys('pwd')

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([],self.verificationErrors)
if __name__ == '__main__':
	unittest.main()
#mail

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