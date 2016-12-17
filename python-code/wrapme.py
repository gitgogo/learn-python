#coding=utf-8
#包装类、授权属性
class WrapMe(object):
	def __init__(self,obj):
		self.__data=obj
	def get(self):
		return self.__data
	def __repr__(self):
		return 'self.__data'
	def __str__(self):
		return str(self.__data)
	def __getattr__(self,attr):
		return getattr(self.__data,attr)

wrappedList=WrapMe([12,'wewe',23.43]) #列表
wrappedList.append('bar')
wrappedList.append(123)
print wrappedList
print wrappedList.count(123)
print wrappedList.pop()
print wrappedList
print wrappedList.get()[3]

f=WrapMe(open('a.txt','r')) #对文件包装
f.get()
f.readline()
f.tell()
f.close()