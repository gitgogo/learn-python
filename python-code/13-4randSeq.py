#coding=utf-8
#自定义迭代器
from random import choice

class RandSeq(object):
	def __init__(self,seq):
		self.data=seq

	def __iter__(self):
		return self

	def next(self):
		return choice(self.data)

for each in RandSeq(range(10)):
	print each
	if each==3:
		break

#任一项的迭代器
class AnyIter(object):
	def __init__(self,seq,safe=False):
		self.safe=safe
		self.iter=iter(seq)

	def __iter__(self):
		return self

	def next(self,howmany=1):
		retval=[]
		for each in range(howmany):
			try:
				retval.append(self.iter.next())
			except StopIteration:
				if self.safe:
					break
				else:
					raise
		return retval

a = AnyIter(range(10),True)
i = iter(a)
for j in range(1,10):
	print j,':',i.next(j)

