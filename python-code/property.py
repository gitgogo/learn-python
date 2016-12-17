#coding=utf-8
class HideX(object):
	def __init__(self,x):
		self.x=x

	@property	#添加属性property后无法通过构造器赋值
	def x():
		def fget(self):
			return ~self.x
		def fset(self):
			assert isinstance(x,int),"x must be an integer"
			self.__x=~x

		return locals()

ins=HideX(11)
print ins.x
ins.x=12
print ins.x