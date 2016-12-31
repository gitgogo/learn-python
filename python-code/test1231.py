#coding=utf-8
import sys,os
import time
os.chdir('f:\\')
name1=time.strftime('%Y-%m-%d')
os.mkdir(name1)
os.chdir(name1)
name2=str(time.localtime().tm_hour)
os.mkdir(name2)
os.chdir(name2)
name3=str(time.localtime().tm_min)
os.mkdir(name3)
os.chdir(name3)
name4=str(time.localtime().tm_sec)
os.mkdir(name4)
os.chdir(name4)
with open('time.txt','w') as f:
	f.write(time.strftime('%Y-%m-%d %H:%M:%S'))

#异常处理
while True:
	try:
		# int(raw_input('input a num: '))
		num=raw_input('input a number: ')
		assert num in '0123456789'
		break
	except Exception,e:
		print 'must be int\n',type(e)
#python
try:
	with open('12.txt') as f:
		print f.read()
except:
	with open('12.txt','w') as f:
		f.writelines(['glory road!\n']*2)
#raise ValueError
def try_except():
	for i in range(4):
		print i,
		if i==2:
			raise ValueError
try:
	try_except()
except (ValueError,IOError,NameError),e:
	print e
#文件异常
try:
  fh = open("c:\testfile", "r")
  try:
    content = fh.read()
    print content
  finally:
    print u"关闭文件"
    fh.close()
except IOError:
  print u"Error: 没有找到文件或读取文件失败"
 #
 import sys
try:
  s = raw_input('Enter something --> ')
except KeyboardInterrupt:
  print '\nWhy did you do an Ctrl+c on me?' #ctrl+c
  sys.exit() # exit the program
except:
  print '\nSome error/exception occurred.' #ctrl+z 报错
else:
  print "no exception occur!"
finally:
  print "finally is executed!"
#文件异常
try:
  fh = open("f:\\test\\1.txt", "r")
  try:
    content = fh.read()
    print content
  finally:
    print u"关闭文件"
    fh.close()
except IOError:
  print u"Error: 没有找到文件或读取文件失败"

#自定义异常
class ShortInputException(Exception):
  '''A user-defined exception class.'''
  def __init__(self, length, atleast):
    Exception.__init__(self)
    self.length = length
    self.atleast = atleast
try:
  s = raw_input('Enter something --> ')
  if len(s) < 3:
    #如果输入的内容长度小于3，触发异常
    raise ShortInputException(len(s), 3)
except EOFError:
  print '\nWhy did you do an EOF on me?'
except ShortInputException, x:
  print 'ShortInputException: The input was of length %d, \
  was expecting at least %d' % (x.length, x.atleast)
else:
  print 'No exception was raised.'

#with实现方式
class opened(object):
  def __init__(self, filename):
    self.handle = open(filename)
    print 'Resource: %s' % filename
  def __enter__(self):
    print '[Enter %s]: Allocate resource.' % self.handle
    return self.handle   # 可以返回不同的对象
  def __exit__(self, exc_type, exc_value, exc_trackback):
    print '[Exit %s]: Free resource.' % self.handle
    if exc_trackback is None:
      print '[Exit %s]: Exited without exception.' % self.handle
    else:
      print '[Exit %s]: Exited with exception raised.' % self.handle
      return False   # 可以省略，缺省的None也是被看做是False
    self.handle.close()

with opened(r'f:\\1.txt') as fp:
  for line in fp.readlines():
    print(line)