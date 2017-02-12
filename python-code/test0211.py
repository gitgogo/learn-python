#coding=utf-8
class Province:

    country = 'China'

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args, **kwargs):
        print 'func'
# 获取类的成员，即：静态字段、方法、
print Province.__dict__

obj1 = Province('HeBei',10000)
print obj1.__dict__
# 获取 对象obj1 的成员
# 输出：{'count': 10000, 'name': 'HeBei'}

obj2 = Province('HeNan', 3888)
print obj2.__dict__
# 获取 对象obj1 的成员
# 输出：{'count': 3888, 'name': 'HeNan'}

class Foo:

    def __str__(self):
        return 'gloryroad'
        # print 'hello'

obj = Foo()
# obj
str(obj)

class Foo:

    def __init__(self):
        pass
    
    def __call__(self, *args, **kwargs):

        return sum(args)+sum(kwargs.values())

obj = Foo() # 执行 __init__
print obj(1,2,3,t=4,e=5) # 执行 __call__
print Foo.__dict__
#字典操作
class Foo(object):
	def __init__(self,d):
		self.d=d
 
	def __getitem__(self, key):
		print '__getitem__',d[key]
 
	def __setitem__(self, key, value):
        # print '__setitem__',key,value
		d[key]=value
 
	def __delitem__(self, key):
		print '__delitem__',key
		del d[key]
d={}
obj = Foo(d)
# obj['k1']      # 自动触发执行 __getitem__
obj['k2'] = 'wupeiqi'   # 自动触发执行 __setitem__
obj['k1']='hhhh'
obj['k1']
obj['k2']
# del obj['k1']           # 自动触发执行 __delitem__
#切片操作
class Foo(object):
	def __init__(self,st):
		self.st=st

	def __getslice__(self, i, j):
		print '__getslice__',self.st[i:j]
 
	def __setslice__(self, i, j, sequence):
		# print '__setslice__',st[i:j]=sequence
		self.st[i:j]=sequence
 
	def __delslice__(self, i, j):
		print '__delslice__',i,j
		del self.st[i:j]

obj = Foo(list('helloone'))
obj[2:6]=['1','2','3','4']
obj[2:6]
# obj[-1:1]                   # 自动触发执行 __getslice__
# obj[0:1] = [11,22,33,44]    # 自动触发执行 __setslice__
# del obj[0:2]  

#迭代器
class Foo(object):
    def __init__(self, sq):
        self.sq = sq

    def __iter__(self):
        return iter(self.sq.values())

obj = Foo({'w':1,'q':2})

for i in obj:
    print i

#new方法
class A(object): 
    def __init__(self): 
        print "init"
    def __new__(cls,*args, **kwargs): 
        print "new %s"%cls
        return object.__new__(cls, *args, **kwargs) 

#单例模式--只能生成唯一的实例
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1

one = MyClass()
two = MyClass()

two.a = 3
print one.a
#3
#one和two完全相同,可以用id(), ==, is检测
print id(one)
#29097904
print id(two)
#29097904
print one == two
#True
print one is two
#True

class Class(object):
	def __init__(self,*args,**kw):
		self.args=args
		self.kw=kw

	def get_in(self):
		return self.args,self.kw

a=Class(1,2,3,4,t=5)
print a.get_in()

#查看引用次数
import sys
print sys.getrefcount(500111)
a = 5001111      # 创建对象<5001111>
print sys.getrefcount(a)

#循环引用--可被垃圾回收
class LeakTest:
        def __init__(self):
                self.a = None
                self.b = None
                print "object = %d born here." % id(self)

A = LeakTest()
B = LeakTest()
A.a = B
B.b = A

import sys
print sys.getrefcount(A)
print sys.getrefcount(B)

del A
try:
    print sys.getrefcount(A)
except Exception,e:
    print e

del B
try:
    print sys.getrefcount(B)
except Exception,e:
    print e

#闭包
def outer() :
  name = "python"
  a=2
  def inner() :
    print name,a
  return inner

res = outer()
res()
print res.func_closure
