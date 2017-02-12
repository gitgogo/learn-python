#coding=utf-8
# outerVar = "this is a global variable"
# a=3
# def test() :
#   b=4
#   innerVar = "this is a Local variable"
#   print "local variables :"
#   print locals()
#   print globals()

# test()
# print "global variables :"
# print globals()
# print locals()
#coding=utf-8

# def outer() :
#   name = "python"
#   def inner() :
#     print name
#   return inner()

# import time
# # #定义装饰器
# def log(func):
#   def wrapper(*args, **kw):
#     # print 'call func is %s' %func.__name__
#     # with open('f:\\11.txt','w') as f:
#     # 	f.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
#     start=time.time()
#     func(*args, **kw)
#     print time.time()-start
#   return wrapper

# @log 
# def now():
#     with open('f:\\11.txt') as f:
#     	print f.read()
#     time.sleep(2)
# now()

# def deco(func):
#     print "before myfunc() called."
#     func()
#     print "  after myfunc() called."
#     return func

# def myfunc():
#     print " myfunc() called."

# myfuncc = deco(myfunc)
# myfuncc()
# myfuncc()
###########
# def deco(func):
#     def _deco():
#         print "before myfunc() called."
#         func()
#         print "  after myfunc() called."
#         # 不需要返回func，实际上应返回原函数的返回值
#     return _deco

# @deco  #myfunc=(deco(myfunc))
# def myfunc():
#     print " myfunc() called."

# myfunc()
# myfunc()
###############
# def log(func):
#   def wrapper(*args, **kw):
#     print 'call func is %s' %func.__name__
#     return func(*args, **kw)
#   return wrapper

# @log 
# def now():
#     now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
#     print "current time is %s" %now
# now()
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
# def deco(func):
#     def _deco(a, b):
#         print "before myfunc() called."
#         ret = func(a, b)
#         print "  after myfunc() called. result: %s" % ret
#         return ret
#     return _deco
 

# def myfunc(a, b):
#     print " myfunc(%s,%s) called." % (a, b)
#     return a + b
 
# deco(myfunc)(1,2)
# deco(myfunc)(3,4)

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