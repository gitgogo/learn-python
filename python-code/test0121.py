#coding=utf-8
class UniversityMember(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def getName(self):
		return self.name

	def getAge(self):
		return self.age

class Student(UniversityMember):
	def __init__(self,name,age,sno,depart):
		UniversityMember.__init__(self,name,age)
		self.sno=sno
		self.depart=depart

	def getSno(self):
		return self.sno

	def getDepartment(self):
		return self.depart

s=Student('jack',20,012,'DD')
print s.name,s.age
s.name='spiderman'
print s.getName()
