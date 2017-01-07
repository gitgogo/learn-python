#coding=utf-8
import time
import datetime
print datetime.date.today()

#获取当前时间的时间戳
now = time.time()
print now
#将时间戳转换为date类型的时间
s = datetime.date.fromtimestamp(now)
print s