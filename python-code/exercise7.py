# #coding=utf-8
# 1、实现自己的数学模块mymath，提供有4个函数，分别为加减乘除， 在B模块中调用A模块的函数。
def sum1(*argv):
	return sum(argv)
def minus(*argv):
	result=argv[0]
	if len(argv)==1:
		return result
	else:
		for i in range(1,len(argv)):
			result-=argv[i]
		return result
def multi(*argv):
	result=1
	for i in argv:
		result*=i
	return result
def div(*argv):
	result=argv[0]
	if len(argv)==1:
		return result
	else:
		for i in range(1,len(argv)):
			result/=float(argv[i])
		return result

from exercise7 import *
print sum1(3,2,1,4)
print minus(3,2,1,4)
print multi(3,2,1,4)
print div(3,2,1,4)

# 2、实现自己的字符串模块mystr，里面有方法:isdigit,strip, join,split 

# 3、构建一个模块的层级包


# 4、实现一个除法函数，并处理异常 
def div(n1,n2):
	try:
		return round(float(n1)/n2,3)
	except ZeroDivisionError,e:
		print e 

# 5、引发一个异常，并将它抛除到上层函数，上层函数捕获该异常并处理 
def raise_exception():
	num=raw_input('input a number->')
	if num not in string.digits:
		raise TypeError('must be number!')
def hadle():
	try:
		raise_exception()
	except TypeError,e:
		print e

# 6、实现字符串、列表、元组和set之间互相转换 

# 7、结合set对象，统计某个list出现的重复元素个数
def count(lis):
	result={}
	for element in set(lis):
		result[element]=lis.count(element)
	return result
# 8、定义一个元组，向元组中添加元素或者修改已有元素，并捕获异常 
tup=(1,2,3,'r','e')
try:
	tup[1]='w'
except TypeError,e:
	print e

# 9、删除无重复元组中给定的元素

# 10、有一个ip.txt，里面每行是一个ip，实现一个函数，ping 每个ip的结 果，把结果记录存到ping.txt中，格式为ip:0或ip:1 ，0代表ping成功，1 代表ping失败

# 11、实现DOS命令执行功能，接受输入命令并执行，然后把执行结果和 返回码打印到屏幕

# 12、求一个n*n矩阵对角线元素之和
import random
def sum_nn(n):
	result=0
	listn=[]
	for i in range(n):
		lis=[]
		for j in range(n):
			lis.append(random.randint(1,10))
		listn.append(lis)
	for i in range(n):
		result+=listn[i][i]
	return result

# 13、输入一个数组，最大的与第一个元素交换，最小的与最后一个元素 交换，输出数组
def change_list(lis):
	max_dex=lis.index(max(lis))
	min_dex=lis.index(min(lis))
	lis[0],lis[max_dex]=lis[max_dex],lis[0]
	lis[-1],lis[min_dex]=lis[min_dex],lis[-1]
	return lis

# 14、平衡点，一个数组，有一个数字左边所有的数字加起来的总和等于 这个数右边所有数字的总和，请输出这个数以及坐标
import random
def balance(lis):
	for i,j in enumerate(lis,1):
		if sum(lis[:i-1])==sum(lis[i:]):
			return j,i

count=0
while True:
	count+=1
	lis=[random.randint(1,10) for x in range(10)]
	result=balance(lis)
	if result:
		print u'程序在第%s次找到符合的数组：%s平衡点为%s，在第%s个元素'%(count,lis,result[0],result[1])
		break

# 15、将单词表中由相同字母组成的单词归成一类，每类单词按照单词的 首字母排序，并按每类中第一个单词字典序由大到小排列输出各个类别。
# 输入格式:按字典序由小到大输入若干个单词，每个单词占一行，以end 结束输入。
# cinema
# iceman
# maps spam aboard abroad end
# 输出格式:一类单词一行，类别间单词以空格隔开。 aboard abroad
# cinema iceman
# maps spam
content=[]
while True:
	words=raw_input('input words-->')
	content.extend(words.strip().split())
	if words.endswith('end'):
		break
content.remove('end')
content.sort()

for index,word in enumerate(content,1):
	result=[word]
	for mac in content[index:]:
		if sorted(word)==sorted(mac):
			result.append(mac)
			content.remove(mac)
	print ' '.join(result)

# 16、输入一个数组，实现一个函数，让所有奇数都在偶数前面 
def change_list(lis):
	tmp=[]
	for element in lis:
		if element%2:
			tmp.insert(0,element)
		else:
			tmp.append(element)
	return tmp
# 17、lista=['a','abc','d','abc','fgi','abf']，寻找列表中第一次出现次数最多的
# 第一个字母，出现了几次

# 18、请输入星期几的第一个字母来判断一下是星期几，如果第一个字母 一样，则继续判断第二个字母
week={'m':'monday','t':'tuesday','w':'wednesday','t':'Thursday','f':'Friday','s':{'a':'Saturday','u':'sunday'}}
s=raw_input('input an alpha->').lower()
if s in week.keys() and s!='s':
	print week[s]
elif s=='s':
	s1=raw_input('input the second alpha->').lower()
	if s1 in 'au':
		print week['s'][s1]
	else:
		print 'invalid!'
else:
	print 'invalid!'

# 19、有一堆100块的石头，2个人轮流随机从中取1-5块，谁取最后一块就 谁win，编程实现此过程
n=100
a=0
print 'A first...'
while n>0:
	n-=random.randint(1,6)
	a+=1
if a%2:
	print 'A win!'
else:
	print 'B win!'
# 20、实现一个方法，判断一个正整数是否是2的乘方，比如16是2的4次方 ，返回True;18不是2的乘方，返回False。要求性能尽可能高
def is2power(n):
	while n>1:
		print n
		if n%2:
			return False
		n=float(n)/2
	else:
		return True
