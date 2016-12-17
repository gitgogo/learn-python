#coding=utf-8
#函数装饰器练习
from time import ctime,sleep

def tsfunc(func):
	def wrappedFunc():
		print '[%s] %s() called'%(ctime(),func.__name__)
		return func()
	return wrappedFunc

@tsfunc#对函数foo进行装饰，打印被调用的时间
def foo():
	pass

for i in range(3):
	foo()
	sleep(1)