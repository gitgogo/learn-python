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
#装饰器实现--准备工作
coding=utf-8
outerVar = "this is a global variable"
a=3
def test() :
  b=4
  innerVar = "this is a Local variable"
  print "local variables :"
  print locals()
  print globals()

test()
print "global variables :"
print globals()
print locals()
coding=utf-8

def outer() :
  name = "python"
  def inner() :
    print name
  return inner()

import time
# # #定义装饰器
def log(func):
  def wrapper(*args, **kw):
    # print 'call func is %s' %func.__name__
    # with open('f:\\11.txt','w') as f:
    # 	f.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    start=time.time()
    func(*args, **kw)
    print time.time()-start
  return wrapper

@log 
def now():
    with open('f:\\11.txt') as f:
    	print f.read()
    time.sleep(2)
now()
###########
def deco(func):
    print "before myfunc() called."
    func()
    print "  after myfunc() called."
    return func

def myfunc():
    print " myfunc() called."

myfuncc = deco(myfunc)
myfuncc()
myfuncc()
###########
def deco(func):
    def _deco():
        print "before myfunc() called."
        func()
        print "  after myfunc() called."
        # 不需要返回func，实际上应返回原函数的返回值
    return _deco

@deco  #myfunc=(deco(myfunc))
def myfunc():
    print " myfunc() called."

myfunc()
myfunc()
##############
def log(func):
  def wrapper(*args, **kw):
    print 'call func is %s' %func.__name__
    return func(*args, **kw)
  return wrapper

@log 
def now():
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print "current time is %s" %now
now()
################
def deco(func):
    def _deco(*args,**kw):
        print "before myfunc() called."
        ret = func(*args, **kw)
        print "  after myfunc() called. result: %s" % ret
        return ret
    return _deco

@deco
def myfunc(a, b):
    print " myfunc(%s,%s) called." % (a, b)
    return a + b

myfunc(1, 2)  #deco(myfunc)(1,2)
myfunc(3, 4)  #deco(myfunc)(3,4)
######
def deco(func):
    def _deco(a, b):
        print "before myfunc() called."
        ret = func(a, b)
        print "  after myfunc() called. result: %s" % ret
        return ret
    return _deco
 

def myfunc(a, b):
    print " myfunc(%s,%s) called." % (a, b)
    return a + b
 
deco(myfunc)(1,2)
deco(myfunc)(3,4)

def deco(func):
    def _deco(*args, **kwargs):
        print "before %s called." % func.__name__
        ret = func(*args, **kwargs)
        print "  after %s called. result: %s" % (func.__name__, ret)
        return ret
    return _deco

@deco
def myfunc(a, b):
    print " myfunc(%s,%s) called." % (a, b)
    return a+b
@deco
def myfunc2(a, b, c):
    print " myfunc2(%s,%s,%s) called." % (a, b, c)
    return a+b+c

myfunc(1, 2)
myfunc(3, 4)
myfunc2(1, 2, 3)
myfunc2(3, 4, 5)

########带参数
def deco(arg):
    def _deco(func):
        def __deco():
            print "before %s called [%s]." % (func.__name__, arg)
            func()
            print "  after %s called [%s]." % (func.__name__, arg)
        return __deco
    return _deco

@deco("mymodule") #deco(myfunc())('mymodule')
def myfunc():
    print " myfunc() called."

@deco("module2")
def myfunc2():
    print " myfunc2() called."

myfunc()
myfunc2()
#装饰器（带参数)
def deco(arg):
	def _deco(func):
		def __deco(*args,**kw):
			print 'before %s called [%s]'%(func.__name__,arg)
			return func(*args,**kw)
			# print 'after %s called [%s]'%(func.__name__,arg)
		return __deco
	return _deco

@deco('module')  # myfunc=deco('module')(myfunc)
def myfunc(a,b):
	print 'myfunc called'
	return a+b

print myfunc(2,3)