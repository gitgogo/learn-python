#coding=utf-8
import os,chardet
path='/Users/ralphliu/Document/'
for file in os.listdir(path):
	if os.path.splitext(file)[1]=='.txt':
		with open(os.path.join(path,file),'a') as f:
			f.write(os.linesep+u'被发现了！'.encode('utf-8'))