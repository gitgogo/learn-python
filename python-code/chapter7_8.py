#coding=utf-8
#将姓名、编号存入字典，按姓名排序输出、按编号排序输出
user={}
for i in range(4):
	name=raw_input('input your name: ')
	num=int(input('input your number: '))
	user[name]=num
for j in sorted(user):
	print j,user[j]

#按字典的value排序，要详细了解下sorted函数的用法
sorted(user.iteritems(),key=lambda x:x[1])

