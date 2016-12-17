#coding=utf-8
import os
for tmpdir in ('/tmp',r'f:\file'):
	if os.path.isdir(tmpdir):
		break
else :
	print 'no temp dir avilable'
	tmpdir=''
if tmpdir:
	os.chdir(tmpdir)
	cwd=os.getcwd()
	print '=====current temporary dir: ',cwd
	print '=====creating example dir...'
	os.mkdir('example')
	os.chdir('example')
	print '=====new working dir:',os.getcwd()
	print '=====original dir listing: ',os.listdir(cwd)
	print '=====creating test file...'
	fobj=open('test','w')
	fobj.write('foot\n')
	fobj.write('bars\n')
	fobj.close()
	cwd=os.getcwd()
	print '=====updated dir listing: ',os.listdir(cwd)

	print '=====renaming "test" to "filetest.txt" '
	os.rename('test','filetest.txt')
	print '=====updated dit listing: ',os.listdir(cwd)

	path=os.path.join(cwd,os.listdir(cwd)[0])
	print 'full file name: ',path
	print '=====(pathname,basename): ',os.path.split(path)
	print '=====(filename,extension): ',os.path.splitext(os.path.basename(path))

	print '=====displaying file contens: '
	fobj=open(path)
	for eachline in fobj:
		print eachline
	fobj.close()

	print '=====deleting test file'
	os.remove(path)
	print '=====updated dir list: ',os.listdir(cwd)
	os.chdir(os.pardir)
	print '=====deleting test dir'
	os.rmdir('example')
	print '=====Down'