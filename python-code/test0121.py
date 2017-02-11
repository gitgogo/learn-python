#coding=utf-8
class Person(object):
	count=0 #
	def __init__(self,name,age):
		self.name=name
		self.age=age
		self.__name='kk'
		Person.count+=1

	def work(self,act):
		return act

	@classmethod
	def function(cls):
		print 'calling classmethod...'

	@staticmethod
	def static_fun():
		print 'calling staticmethod...'

	@property
	def prop(self):
		return self.name

	def __del__(self):
		print 'del called...'

singer=Person('jack',23)
actor=Person('Blues',44)
actor.sex='f'
print singer._Person__name
print getattr(actor,'name')
setattr(actor,'name','Lucy')
print getattr(actor,'name')
print hasattr(actor,'name')
print singer.work('hiting')
print Person.count
del Person.count
# delattr(Person,'count')
# print Person.count
Person.function()
Person.static_fun()
print singer.prop

def set_feather(self,value):
	if value in (True,False):
		self.value=value
	else:
		raise ValueError

#coding=utf-8
class Parent(object): # define parent class 
  parentAttr = 100 
  def __init__(self): 
    "父类构造方法，用于初始化工作"
    print "Calling parent constructor" 

  def parentMethod(self): 
    print 'Calling parent method' 

  def setAttr(self, attr): 
    Parent.parentAttr = attr 

  def getAttr(self): 
    print "Parent attribute :", Parent.parentAttr

class Child1(Parent): # define child1 class 
  def __init__(self): 
    "子类构造方法，用于初始化子类本身数据的工作"
    print "Calling child1 constructor" 

  def childMethod(self):
    print 'Calling child1 method' 
    Parent.parentMethod(self) #调用基类的方法，所以要加上参数self
class Child2(Parent): # define child2 class 
  #没有实现__init__方法，则会调用基类的__init__方法
  def childMethod(self): 
    print 'Calling child2 method' 
    self.parentMethod()  #子类调用自己从父类那继承过来的父类的方法

c1 = Child1() # 实例化子类 1
c2 = Child2() # 实例化子类 2
c1.childMethod() # 调用子类1的方法
c2.childMethod() # 调用子类2的方法
c1.parentMethod() # 子类实例对象调用父类方法
c1.setAttr(200) # 再次调用父类的方法
c1.getAttr() # 再次调用父类的方法

#继承类
class UniversityMember(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
 
    def getAge(self):
        return self.age

class Student(UniversityMember):
    def __init__(self, name, age, sno, Department):
        #注意要显示调用父类构造方法，并传递参数self
        UniversityMember.__init__(self, name, age) 
        self.sno = sno
        self.Department = Department
 
    def getSno(self):
        return self.sno
 
    def getDepartment(self):
        return self.Department

s = Student("fosterwu", "18", "CS", 18)
print s.name, s.age
s.name = 'superman'
print s.name
print s.getName()
print s.getAge()

#property
import os
class Person(object):
    def __init__(self,name):
        self.Name = name
    def getName(self):
        print 'fetch...'
        return self.Name
    def setName(self, name):
        print 'change...'
        self.Name = name
    def delName(self):
        print 'remove...'
        del self.Name
    name = property(getName,setName,delName,'name property docs')
    # name=property(getName,setName)

bob = Person('Bob Smith')
print bob.name
bob.name = 'Robert Smith'
print bob.name
del bob.name
#封装
class Animal(object):

    def __init__(self, name): 
#构造方法一个对象创建后会立即调用此方法
        self.Name = name
        print self.Name

    def accessibleMethod(self):
 #绑定方法对外公开
        print "I have a self! current name is:"
        print self.Name
        print "the secret message is:"
        self.__inaccessible()

    def __inaccessible(self):
 #私有方法对外不公开以双下划线开头
        print "U cannot see me..."

    @staticmethod
    def staticMethod():
# self.accessibleMethod() #在静态方法中无法
#直接调用实例方法直接抛出NameError异常
        print "this is a static method"
    def setName(self,name): #访问器函数
        print "setName:"
        self.Name=name

    def getName(self): #访问器函数
        print "getName:"
        return self.Name

a = Animal("learns")
print a.getName()
a.setName("sr")
print "new name:",a.getName()
a.staticMethod()
Animal.staticMethod()

class Student():
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.__score=score

	def setScore(self,score):
		try:
			if not isinstance(score,int):
				raise ValueError('score must be integer')
			if score<0 or score>100:
				raise ValueError('score must be between 0-100')
			self.__score=score
		except Exception,e:
			print e

	def getScore(self):
		return self.__score

stu=Student('jack',12,89)
# print stu.getScore()
stu.setScore(560)
print stu.getScore()
#多态
class calculator:
	def count(self,args):
		return 1
calc=calculator()
#自定义类型
from random import choice
#obj是随机返回的类型不确定
obj=choice(['hello,world',[1,2,3],calc])
print obj
print type(obj)
print obj.count('a') #方法多态

#运算符重写
class Vector(object) :
  def __init__(self, a, b) :
    self.a = a
    self.b = b
  def __str__(self): 
    return 'Vector (%d, %d)' % (self.a, self.b)
  def __add__(self,other) :
    return Vector(self.a + other.a, self.b + other.b)

x =  Vector(3,7)
y =  Vector(1, -10)
print x + y
print str(x)
# =======
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
