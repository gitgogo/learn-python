#coding=utf-8
'''高级闭包和装饰器的例子：用户选择在函数调用之前或者之后，把函数调用写入日志中'''
from time import time

def logged(when):
	def log(f,*args,**kargs):
		print 'Called:\n function: %s\n args: %r\n kargs: %r'%(f,args,kargs)

	def pre_logged(f):
		def wrapper(*args,**kargs):
			log(f,*args,**kargs)
			return f(*args,**kargs)
		return wrapper

	def post_logged(f):
		def wrapped(*args,**kargs):
			now=time()
			try:
				return f(*args,**kargs)
			finally:
				log(f,*args,**kargs)
				print ' time delta: %s'%(time()-now)
		return wrapped
	try:
		return {'pre':pre_logged,'post':post_logged}[when]
	except KeyError ,e:
		raise ValueError(e),'must be "pre" or "post"'

@logged('post')
def hello(name):
	print 'Hello, ',name

hello('Ralph')