#coding=utf-8
'''判断是否闰年,可以被4整除，但不能被100整除，或者既可以被4又可以被100整除
11-8 使用filter进行函数式编程'''
#判断是否闰年
def is_leap(y):
	if (y%4==0 and y%100!=0) or (y%4==0 and y%100==0):
		return True
	else:
		return False
#使用filter过滤输出闰年
def leap_year(year):
	return filter(is_leap,year)
print leap_year([2008,2010,2011,1988,1989,2016])
#使用列表解析式
print [x for x in range(1988,2017) if is_leap(x)]

#reduce函数编程,实现累加和，平均值，阶乘
print reduce(lambda x,y:x+y,range(1,101))
print reduce(lambda x,y:x+y,range(1,101))/100.0