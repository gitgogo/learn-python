#coding=utf-8
class a(object):
	def __init__(self):
		print 'init...'

	def __new__(cls,*arg):
		print 'new...'
		return object.__new__(cls,*args)

	def s(self):
		print 123

# print a.__dict__
b=a()
b.s()