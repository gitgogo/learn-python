#coding=utf-8
#使用文件来存储属性
import os
import pickle

class FileDescr(object):
	saved=[]

	def __init__(self,name=None):
		self.name=name

	def __get__(self,obj,typ=None):
		if self.name not in FileDescr.saved:
			raise AttributeError,"%r used before assignment"%self.name
		try:
			f=open(self.name,'r')
			val=pickle.load(f)
			f.close()
			return val
		except (pickle.UnpicklingError,IOError,EOFError,AttributeError,ImportError
			,IndexError),e:
			raise AttributeError,"could not read %r:%s"%(self.name,e)

	def __set__(self,obj,val):
		f=open(self.name,'w')
		try:
			try:
				pickle.dump(val,f)
				FileDescr.saved.append(self.name)
		except (TypeError,pickle.PickingError),e:
			raise AttributeError,"could not pickle %r"%self.name
		finally:
			f.close()

	def __delete__(self,obj):
		try:
			os.unlink(self.name)#Remove a file (same as remove(path)).
			FileDescr.saved.remove(self.name)
		except (OSError,ValueError),e:
			pass