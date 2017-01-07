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