#coding=utf-8
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
	def __init__(self,name,sex,lenth,num):
		super(Dog,self).__init__(name,sex,lenth)
		self.num=num

	def hello(self):
		super(Dog,self).say_hello()	

dogg=Dog('X','m',57,44)
print dogg.num
dogg.hello()
print Dog.__name__,Dog.__doc__,dogg.__dict__,Dog.__bases__,Dog.__module__

dog=Animal('dog','f',78)
# Animal.class_method(5)
# Animal.static_method(5)
# dog.prop
dog.color='red'
dog.name='Dobby'
del dog.sex
# print dog.name,dog.color
# print dir(dog)
print getattr(dog,'name')
setattr(dog,'name','Doge')
print getattr(dog,'name')
print hasattr(dog,'sex')
delattr(dog,'color')
print getattr(dog,'color',404)

#操作文件的类

class op_file(object):
    def __init__(self,file_path):
        self.file_path=file_path
        
    def get_file_handler(self):
        try:
            self.fp=open(self.file_path,"r")
            return self.fp
        except Exception,e:
            print e

    def get_file_line_content(self,line_number):
        number=1
        for line in self.get_file_handler():
            if line_number==number:
                return line
            number+=1
    def get_cursor_position(self):
        return self.fp.tell()
        
    def close_file(self):
        self.fp.close()


f=op_file("e:\\a.txt")
print f.get_file_line_content(3)
print f.get_cursor_position()

class Foo:

    def __init__(self, name):
        self.name = name

    def ord_func(self):
        """ 定义普通方法，至少有一个self参数 """

        # print self.name
        print u'普通方法'

    @classmethod
    def class_func(cls):
        """ 定义类方法，至少有一个cls参数 """

        print u'类方法'

    @staticmethod
    def static_func():
        """ 定义静态方法 ，无默认参数"""

        print u'静态方法'
foo=Foo('Jim')
foo.ord_func()
Foo.class_func()
Foo.static_func()

# class HandleFile(object):
# 	def __init__(self,filename):
# 		self.filename=filename

# 	def get_line(self,num):
# 		with open(self.filename,'r') as f:
# 			for linenum,line in enumerate(f,1):
# 				if linenum==num:
# 					return line

# file1=HandleFile('f:\\1.txt')
# print file1.get_line(5)

#随机生成10个数、10个字母、10个数字加字母
# class Genera(object):
# 	def __init__(self,num_range,alph_range):

class Goods(object):

	def __init__(self):
		self.value=None

	@property
	def price(self):
		if self.value<100:
			self.price=0
		else:
			self.price=1
		return self.value

	@price.setter
	def price(self, value):
		self.value=value

	@price.deleter
	def price(self):
		print '@price.deleter'

obj = Goods()

# print obj.price  # 自动执行 @property 修饰的 price 方法，并获取方法的返回值
obj.price = 232  # 自动执行 @price.setter 修饰的 price 方法，并将  123 赋值给方法的参数
print obj.price
del obj.price    # 自动执行 @price.deleter 修饰的 price 方法

class f(object) :
  count = 12#类变量

t = f()
t.count=13
print u"t.count内存地址 =", id(t.count), "t.count =", t.count
print u"f.count内存地址 =", id(f.count), "f.count =", f.count
del t.count
print u"通过实例对象修改count的值后"
print u"t.count内存地址 =", id(t.count), "t.count =", t.count
print u"f.count内存地址 =", id(f.count), "f.count =", f.count
#不同变量类型
sex="male"
class Person(object):
    id = 12   #类静态成员在这儿定义，注意缩进
    def  __init__(self,name):
        self.name = name #类的实例变量
        self.inName = 'ads' #类的实例变量
    def getName(self) :
        global sex
        name = "lucy" #局部变量
        return self.name, name,sex
p = Person('linda')
print p.name #访问对象的实例变量
#通过函数访问实例变量和局部变量
res = p.getName()
print res
#类方法
class Person(object):
    id = 12   #类静态成员在这儿定义，注意缩进
    def  __init__( self,name ):
        self.name = name
        self.__inName = 'ads' 
 
    @classmethod   #类方法定义，用注解方式说明
    def up(cls,a ):   #这儿是cls，不是self
        print cls,cls.__name__
        return a+1

#创建类的实例
p = Person( "alpha" )
#调用类方法
print Person.up(20) #类名直接调用
print p.up(12) #通过实例对象调用

#私有变量
class Person(object):
    __secretCount = 0 #私有属性
    def  __init__(self, name):
        self.name = name #实例属性
        self.__inName = 'ads' #私有属性

    def visit_private_attribute( self ):
        self.__secretCount += 1
        print "__secretCount: ", self.__secretCount
        print u"__inName：", self.__inName
p = Person("prel")
p.visit_private_attribute()
print u"在类外直接通过实例访问私有属性"
print p.__inName #exception
print p._Person.__inName #ok