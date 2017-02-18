#coding=utf-8
class LikeDict(object):
	def __init__(self,attribut):
		self.attribut=attribut

	def __getitem__(self,key):
		print self.attribut[key]

	def __setitem__(self,key,value):
		self.attribut[key]=value

	def __delitem__(self,key):
		del attribut[key]

Dict={}
likeDict=LikeDict(Dict)
likeDict['a']=1
likeDict['b']=2
likeDict['b']
likeDict['a']