#coding=utf-8
#统计一个文件有多少行，忽略以#开头的行
f=open('8-2.py','r')
n=0
for lines in f:
	if not lines.startswith('#'):
		n+=1
f.close()
print n