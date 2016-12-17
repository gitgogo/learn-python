#coding=utf-8
#下载一个web页面，显示html文件第一个和最后一个非空格行
from urllib import urlretrieve

def firstNonBlank(lines):
	for line in lines:
		if not line.strip():
			continue
	else: return line

def firstLast(webpage):
	f=open(webpage)
	lines=f.readlines()
	f.close()
	print firstNonBlank(lines)
	lines.reverse()
	print firstNonBlank(lines)

def download(url='http://www.baidu.com',process=firstLast):
	try:
		retval=urlretrieve(url)[0]
	except IOError :
		retval=None
	if retval:
		process(retval)

if __name__=='__main__':
	download()