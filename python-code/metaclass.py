#coding=utf-8
#元类
from warnings import warn

class ReqStrSugRepr(type):
	def __init__(cls,name,bases,attrd):
		super(ReqStrSugRepr,cls).__init__(name,bases,attrd)

		if '__str__' not in attrd:
			raise TypeError("class requires overriding of __str__()")

		if '__repr__' not in attrd:
			warn('class suggests overriding of __repr__()\n',stacklevel=3)

print '***defined ReqStrSugRepr (meta)class\n'

class Foo(object):
	__metaclass__=ReqStrSugRepr

	def __str__(self):
		return 'Instance of class:',self.__class__.__name__

	def __repr__(self):
		return self.__class__.__name__

print '***defined Foo class\n'

class Bar(object):
	__metaclass__=ReqStrSugRepr

	def __str__(self):
		return 'Instance of class:',self.__class__.__name__

print '***defined Bar class\n'

class FooBar(object):
	__metaclass__=ReqStrSugRepr

print '***defined FooBar class\n'
