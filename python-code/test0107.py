#coding=utf-8
import time
#统计文件中不重复的单词的个数，单词set练习
with open('f:\\1.txt') as f:
	words=f.read().split()
	print len(set(words)),' '.join(set(words))

#enumerate() 添加索引序号
for i,j in enumerate(set([9,8,7,6,5])):
	print i,j

#时间模块
time.strftime('%y年%m月%d天 %H时%M分%S秒'.decode('utf-8').encode('gbk'),time.localtime())

#创建一个时间字符串变量stime
stime = "2015-08-24 13:01:30"
#通过strptime()函数将stime转化成strcut_time形式
formattime = time.strptime(stime,"%Y-%m-%d %H:%M:%S")
print formattime
#遍历返回的时间元组序列
for i in formattime :
	print i,
#datetime
#获取当前时间的时间戳
now = time.time()
print now
#将时间戳转换为date类型的时间
s = datetime.date.fromtimestamp(now)
print s
#天数
#获取今天的日期
today = date.today()
print today

#在今天的日期上再加10天
print today + timedelta(days = 1000)

d1=datetime.datetime(2017,1,9)
d2=datetime.datetime(2016,12,25)
print (d1-d2).days

now=datetime.datetime.now()
print now

delta=datetime.timedelta(days=1)
newTime=now+delta
print newTime,type(newTime)
print newTime.strftime('%Y-%m-%d %H:%M:%S')

print datetime.datetime.now()+datetime.timedelta(days=100)
print datetime.datetime.now()-datetime.timedelta(hours=30)
print datetime.timedelta(hours=1,seconds=20).total_seconds()

#coding=utf-8
import time,datetime,calendar,os
# print [x for x in dir(calendar.Calendar) if not x.startswith('_')]
# print [x for x in dir(calendar) if not x.startswith('_')]
# my_cal=calendar.HTMLCalendar(calendar.MONDAY)
# print my_cal.formatmonth(2017,1)
# with open('/Users/ralphliu/Document/mycal.html','w') as f:
# 	f.write(my_cal.formatmonth(2017,1))

# start_time=time.time()
# fp=open('f:\\tmp.rmvb','wb')
# file=u'f:\\电影\\猎头者BD中字1280高清.rmvb'
# with open(file,'rb') as f:
# 	for line in f:
# 		tmp=line
# # fp.close()
# total_time=time.time()-start_time
# print u'文件大小：%s  用时：%s'%(os.path.getsize(file),total_time)
# def get_date():
# 	return time.strftime('%Y||%m||%d',time.localtime())

# def get_time():
# 	return time.strftime('%H%%%M%%%S',time.localtime())

# def get_date_and_time():
# 	return time.strftime('%Y||%m||%d   %H%%%M%%%S',time.localtime())

# print get_date()
# print get_time()
# print get_date_and_time()

# format_time=time.strptime('2017||01||10   21%45%15','%Y||%m||%d   %H%%%M%%%S')
# print time.mktime(format_time)

import os,time
def make_dir(path):
	os.chdir(path)
	# name_one=str((datetime.datetime.now()-datetime.timedelta(days=300)).year)
	name_one=str(time.localtime().tm_year-1)
	os.mkdir(name_one)
	os.chdir(name_one)
	name_two=str(time.localtime().tm_mon-1)
	if name_two=='0':
		name_two='12'
	os.mkdir(name_two)
	os.chdir(name_two)
	name_three=str(datetime.date.today())
	os.mkdir(name_three)
	file_name=time.strftime('%H%M%S')
	with open(os.path.join(name_three,file_name)+'.txt','w') as f:
		f.write(u'今天是今年的第%s天'%(time.localtime().tm_yday)+
			'\n'+u'今年的第%s周'%(time.strftime('%U')))
make_dir('f:\\')
