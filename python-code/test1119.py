#coding=utf-8
from time import time,sleep
def swap(s):
	u'''hello world i am doc 帮助文档'''
	start_time=time()
	result=''
	for i in s:
		sleep(0.1)
		num=ord(i)
		if 97<=num<=121:
			result+=chr(num-32)
		elif 48<=num<=57:
			result+=i
		else:
			result+=chr(num+32)
	end_time=time()
	timeup=end_time-start_time
	return result,timeup

print swap('helloDJ34')

def random_num():
	return randrange(10)+1

print random_num()+10

def len_str(s):
	count=0
	for i in s:
		count+=1
	return count

# print len_str('hello')
#全局、局部变量
# num=10  #全局变量
# print id(num)
# def a(num):
#      print num  #局部变量
#      print id(num)

# a(5)
# print num  #值为10，全局变量