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

# 8、定义一个元组，向元组中添加元素或者修改已有元素，并捕获异常 

# 9、删除无重复元组中给定的元素

# 10、有一个ip.txt，里面每行是一个ip，实现一个函数，ping 每个ip的结 果，把结果记录存到ping.txt中，格式为ip:0或ip:1 ，0代表ping成功，1 代表ping失败

# 11、实现DOS命令执行功能，接受输入命令并执行，然后把执行结果和 返回码打印到屏幕

# 12、求一个n*n矩阵对角线元素之和

# 13、输入一个数组，最大的与第一个元素交换，最小的与最后一个元素 交换，输出数组

# 14、平衡点，一个数组，有一个数字左边所有的数字加起来的总和等于 这个数右边所有数字的总和，请输出这个数以及坐标

# 15、将单词表中由相同字母组成的单词归成一类，每类单词按照单词的 首字母排序，并按每类中第一个单词字典序由大到小排列输出各个类别。
# 输入格式:按字典序由小到大输入若干个单词，每个单词占一行，以end 结束输入。
# cinema
# iceman
# maps spam aboard abroad end
# 输出格式:一类单词一行，类别间单词以空格隔开。 aboard abroad
# cinema iceman
# maps spam

# 16、输入一个数组，实现一个函数，让所有奇数都在偶数前面 

# 17、lista=['a','abc','d','abc','fgi','abf']，寻找列表中第一次出现次数最多的
# 第一个字母，出现了几次

# 18、请输入星期几的第一个字母来判断一下是星期几，如果第一个字母 一样，则继续判断第二个字母

# 19、有一堆100块的石头，2个人轮流随机从中取1-5块，谁取最后一块就 谁win，编程实现此过程

# 20、实现一个方法，判断一个正整数是否是2的乘方，比如16是2的4次方 ，返回True;18不是2的乘方，返回False。要求性能尽可能高

