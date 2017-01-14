#coding=utf-8
# import tmp
class Animal(object):
	'''this is an Animal classobj test....'''
	count=0 #类变量，全局变量
	def __init__(self,name,sex,lenth):
		self.name=name
		self.sex=sex
		self.lenth=lenth
		Animal.count+=1

	def say_hello(self): #实例方法，普通方法
		print 'hello,',self.name

	@classmethod #定义类方法
	def class_method(cls,num):
		print 'hello,',cls.count+num

	@staticmethod #定义静态方法
	def static_method(num):
		print 'hello,',Animal.count+num

	@property #定义属性
	def prop(self):
		return self.say_hello()

#类继承
class Dog(Animal):
	'''this is an Animal's subclass classobj test....'''
	def __init__(self,name,sex,lenth,num):
		super(Dog,self).__init__(name,sex,lenth)
		self.num=num

	def hello(self):
		super(Dog,self).say_hello()

dogg=Dog('X','m',57,44)
# print Dog.__name__,Dog.__doc__,dogg.__dict__,Dog.__bases__,Dog.__module__

dog=Animal('dog','f',78)
# Animal.class_method(5)
# Animal.static_method(5)
# dog.prop
dog.color='red'
dog.name='Dobby'
del dog.sex
# print dog.name,dog.color
# print dir(dog)
# print getattr(dog,'name')
# setattr(dog,'name','Doge')
# print getattr(dog,'name')
# print hasattr(dog,'sex')
# delattr(dog,'color')
# print getattr(dog,'color',404)

class employee(object) : 
  city = 'BJ' #类属性

  def __init__(self, name) :
    self.name = name #实例变量

  #定义类方法
  @classmethod
  def getCity(cls) :
    return cls.city

  #定义类方法
  @classmethod
  def setCity(cls, city) :
    cls.city = city

  #实例方法
  def set_City(self, city) :
    employee.city = city
emp = employee('joy') #创建类的实例
print emp.getCity() #通过实例对象引用类方法
print employee.getCity()#通过类对象引用类方法

emp.setCity('TJ')#实例对象调用类方法改变类属性的值
print emp.getCity()
print employee.getCity()

employee.setCity('CD')#类对象调用类方法改变类属性的值
print emp.getCity()
print employee.getCity()

emp.set_City('SH')#调用实例方法改变类属性的值
print emp.getCity()
print employee.getCity()

employee.city = 20 #直接修改类属性的值
print emp.getCity()
print employee.getCity()

class Person(object):
    id = 12   #类静态成员在这儿定义，注意缩进
    def  __init__( self,name ):
        self.name = name
        self.__inName = 'ads'

    @staticmethod    #类静态方法定义，用注解方式说明
    def down( b ):   #静态方法不需要self，cls变量
        id = 13
        print u"类变量id =", id
        return b-1

#创建类的实例
p = Person( "alpha" )

#调用静态方法
print Person.down(15) #类名直接调用
print p.down(19) #通过实例对象调用
