#coding=utf-8
#特殊方法定制类，覆盖__str__() __repr__()方法
class RoundFloatManual(object):
	def __init__(self,val):
		assert isinstance(val,float),"Value must be a float!"
		self.value=round(val,2)
	def __str__(self):
		return '%.2f' % self.value
	__repr__=__str__

rfm=RoundFloatManual(5.697)
print rfm
#使用特殊方法__add__() __iadd__()定制类
class Time60(object):
	def __init__(self,hr,min):
		self.hr=hr
		self.min=min
	def __str__(self):
		return '%d:%d'%(self.hr,self.min)
	__repr__=__str__

	def __add__(self,other):
		return self.__class__(self.hr+other.hr,self.min+other.min)
	def __iadd__(self,other):#原位加法，不会创建新的对象，加法前后对象id相同
		self.hr+=other.hr
		self.min+=other.min
		return self

mon=Time60(10,23)
tue=Time60(11,30)
print mon+tue