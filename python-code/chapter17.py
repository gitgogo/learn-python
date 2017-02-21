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