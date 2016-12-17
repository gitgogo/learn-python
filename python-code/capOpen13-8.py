#coding=utf-8
#包装文件对象
class CapOpen(object):
	def __init__(self,fn,mode='r',buf=-1):
		self.file=open(fn,mode,buf)

	def __str__(self):
		return str(self.file)

	def __repr__(self):
		return 'self.file'

	def write(self,line):#修改write方法，始终读入大写
		self.file.write(line.upper())

	def __getattr__(self,attr):
		return getattr(self.file,attr)

#调用
f=CapOpen('/tmp/xxx.txt','w')
f.write('delegation one xxx')
f.close()