#coding=utf-8
# 1、能够熟练进行字符串、列表、元组和set之间的转换。 
set1=set([1,2,'h','e'])
set2=set('hello')
print list(set1),list(set2)
print tuple(set1),tuple(set2)
print str(set1),str(set2)

# 2、结合set对象，统计某个list出现的重复元素个数 
lis=list('helloworld')
dict_e={}
for element in set(lis):
	dict_e[element]=lis.count(element)

# 3、定义一个不可变集合，向不可变集合中添加元素或者修改已有元素， 并捕获异常
frozen_set=frozenset('hello')
try:
	frozen_set.add(1)
	frozen_set.remove('h')
except Exception,e:
	print e

# 4、列出你所有知道的排重方法
obj=list('hellopython112')
#法1
print ' '.join(set(obj))
#法2
for element in obj:
	while obj.count(element)>1:
		obj.remove(element)
print ' '.join(obj)
#法3
print ' '.join(dict.fromkeys(obj).keys())
# 法4
tmp=[]
for element in set(obj):
	if obj.count(element)>1:
		continue
	tmp.append(element)
print ' '.join(tmp)

# 1、计算程序执行耗时
start_time=time.time()
with open(filename) as f:
	for line in f:
		pass
total_time=time.time()-start_time
print total_time
# 2、将时间字符串转换为时间戳 
formattime=time.strptime('2017-01-11','%Y-%m-%d')
print time.mktime(formattime)

# 3、将格式时间字符串转换成时间元组，然后再转换成自定义的时间格式字符串
now='2017-01-11'
struct_time=time.strptime(now,'%Y-%m-%d')
new_time=time.strftime('%Y//%m//%d',struct_time)

# 4、将当前时间戳转换为指定格式日期 
print time.strftime('%Y年%m月%d日 %H时%M分%S秒',time.localtime())

# 5、创建名称为当前时间(年月日)的目录，在这个目录下创建名称为当前时间 
# (年月日)的txt文件，并且输入内容为“你好” 
import os
now=time.strftime('%Y-%m-%d')
os.mkdir(now)
os.chdir(now)
with open(now+'.txt','w') as f:
	f.write(u'你好')

# 6、获得三天(三小时和三分钟)前的时间方法
three_days_ago=datetime.datetime.now()-datetime.timedelta(days=3)
three_hours_ago=datetime.datetime.now()-datetime.timedelta(hours=3)
three_minutes_ago=datetime.datetime.now()-datetime.timedelta(minutes=3)
# 7、计算昨天和明天的日期
print (datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y/%m/%d')
print (datetime.datetime.now()-datetime.timedelta(days=-1)).strftime('%Y/%m/%d')
# 8、使用datetime模块来获取当前的日期和时间 
print datetime.datetime.now()
print datetime.date.today()

# 9、创建名称为log的目录，目录下创建三个文件夹，名分别为去年今天的日期、 当前日期(年月日)、明年今天的日期，
# 然后分别在这三个目录中创建三个.log文 件，名分别为当年的今天在当年中第多少天，文件中分别写入当年的今天是这一年的第几个星期以及当前是星期几
os.chdir('/Users/ralphliu/Document/')
now=datetime.date.today()
for i in range(3):
	dir_name=now.replace(year=now.year-1+i)
	os.mkdir(str(dir_name))
	filename=dir_name.strftime('%j')
	filepath=os.path.join(str(dir_name),filename+'.log')
	with open(filepath,'w') as f:
		f.write(dir_name.strftime('%U')+os.linesep+dir_name.strftime('%A'))


