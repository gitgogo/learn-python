#coding=utf-8
import time,datetime,calendar
# print [x for x in dir(calendar.Calendar) if not x.startswith('_')]
# print [x for x in dir(calendar) if not x.startswith('_')]
my_cal=calendar.HTMLCalendar(calendar.MONDAY)
print my_cal.formatmonth(2017,1)
with open('/Users/ralphliu/Document/mycal.html','w') as f:
	f.write(my_cal.formatmonth(2017,1))