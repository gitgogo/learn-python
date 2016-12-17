#coding=utf-8
# 1、打印2000-3000之间被7整除但不被5整除的数，以，(逗号)分隔 
for num in range(2000,3001):
	if num%5 and not num%7:
		print num,',',

# 2、输出9*9口诀表
for i in range(1,10):
	for j in range(1,i+1):
		print '%dx%d=%d'%(j,i,i*j),
	print

# 3、计算 1 - 1/2 + 1/3 - 1/4 + ... + 1/99 - 1/100 + ...直到最后一项的绝对值小 于10的-5次幂为止 
sum1=0;num=n=1
while abs(num)>=10**-5:
	sum1+=num
	num=1.0/(n+1)*(-1)**n
	n+=1
print sum1

# 4、编程将类似“China”这样的明文译成密文，密码规律是:用字母表中原来的字母后面第4个字母代替原来的字母，不能改变其大小写，如果超出了字母表最后一个字母则回退到字母表中第一个字母
from string import lowercase,uppercase
def transfor(s):
	result=''
	for char in s:
		if char in lowercase:
			if char<'w':
				char=lowercase[lowercase.index(char)+4]
			else:
				char=lowercase[3-len(lowercase)+lowercase.index(char)]
		elif char in uppercase:
			if char<'W':
				char=uppercase[uppercase.index(char)+4]
			else:
				char=uppercase[3-len(uppercase)+uppercase.index(char)]
		result+=char
	return result
print transfor('abcdeABCDE')

# 5、输出以下如下规律的矩阵 
'''
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
'''
for i in range(1,5):
	for j in range(1,6):
		print i*j,
	print

# 6、对一个列表求和，如列表是[4, 3, 6]，求和结果是 [4, 7, 13]，每一项的值 都等与该项的值加上前一项的值
def sum_list(list_num):
	list_sum=[]
	for i in range(len(list_num)):
		list_i=[]
		for j in range(i+1):
			list_i.append(list_num[j])
		list_sum.append(sum(list_i))
	return list_sum
list_num=[4,3,6]
print sum_list([4,3,6])
#two
sum_list=[]
item=0
for i in list_num:
	item+=i
	sum_list.append(item)
print sum_list
#three
lista = [4,3,6,12,56]
for i in xrange(1,len(lista)):
    lista[i] += lista[i-1]
print lista
#four
a=[4, 3, 6,1,2,3,4,5]
b=[]
for i in range(len(a)):
    b.append(reduce(lambda x,y:x+y,a[:i+1]))
print b

# 7、一个字符串 list，每个元素是 1 个 ip，输出出现次数最多的 ip 
def get_most(list_ip):
	mostip=0
	mostip_str=''
	for ip in list(set(list_ip)):
		count=list_ip.count(ip)
		if count>mostip:
			mostip=count
			mostip_str=ip
	return mostip_str,mostip
list_ip=['10.122.67.32','10.122.67.32','10.121.65.22','10.121.69.34','10.121.69.34','10.121.69.34']
print get_most(list_ip)
#字典实现
dict_ip=dict.fromkeys(list_ip,0)
for key in list_ip:
	if key in dict_ip.keys():
		dict_ip[key]+=1
print sorted(dict_ip.items(),key=lambda x:x[1])[-1]
#字典max
dict_ip={}
for i in list(set(list_ip)):
	dict_ip[i]=list_ip.count(i)
print max(dict_ip,key=dict_ip.get)

# 8、打印100以内的素数
from math import sqrt,ceil
def is_prime(num):
	for i in range(2,ceil(sqrt(num))+1):
		if not num%i:
			return False
	return True

print filter(is_prime,range(2,101))
############
num = 2
while num <= 100:
	i = 2
	while i <= int(math.sqrt(num)):
    	if num % i == 0:
        #print str(num) + "不是素数"
      		break
    	i += 1
		if i > int(math.sqrt(num)):
    		print str(num) + u"是素数"
  	num += 1

# 9、实现一个简易版的计算器，功能要求:加、减、乘、除，支持多数同时进 行计算 


# 10、有一分数序列:2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前 20项之和
def fn(n):
	if n==1:
		return 1
	elif n==2:
		return 2
	else:
		return fn(n-1)+fn(n-2)
		
print sum(float(fn(num+1))/fn(num) for num in range(1,20))
#解法2
numerator=2.0
denominator=1.0
sum=0
for i in range(20):
    print numerator,denominator
    sum=sum+numerator/denominator
    numerator,denominator=numerator+denominator,numerator
print sum
# 11、画等(腰)边三角形(实心、空心)
k=1
for i in range(10,21):
	for j in range(i+1):
		if j>i-k:
			print '*',
		else:print ' ',
	k+=2
	print
print '=='*30#==========分割线=============
k=1
for i in range(10,21):
	for j in range(i+1):
		if i<20:
			if j>i-k:
				if i+1-k<j<i:
					print ' ',
				else:print '*',
			else:print ' ',
		else:print '*',
	k+=2
	print

print '=='*30#==========分割线=============
#打印梯形参考
# for i in range(10,21):
# 	for j in range(i):
# 		print '*',
# 	print

# 12、画倒等边三角形
k=0
for i in range(20,9,-1):
	for j in range(i+1):
		if j>=k:
			print '*',
		else:print ' ',
	k+=1
	print

# 13、画直角三角形(实心、空心)
for i in range(10):
	for j in range(i+1):
		print '*',
	print
print '=='*25#==========分割线=============
for i in range(10):
	for j in range(i+1):
		if i<9:
			if j==0 or j==i:
				print '*',
			else:print ' ',
		else:print '*',
	print
# 14、用*号输出字母C的图案
for i in range(10):
	for j in range(8):
		if 0<i<9 and j>0:
			print ' ',
		else:print '*',
	print

# 15、打印N，口，H图案 
#打印正方形
def sqr(n):
	print '* '*n
	for i in range(n-2):
		print '* '+'  '*(n-2)+'*'
	print '* '*n

sqr(4)
#打印N
def N(n):
	for i in range(n):
		if 0<i<n-1:
			print '* '+'  '*(i-1)+'* '+'  '*(n-2-i)+'*'
		else:
			print '* '+'  '*(n-2)+'*'
N(5)
#打印H
def H(n):
	for i in range(n):
		if i==n/2:
			print '* '*n
		else:
			print '* '+'  '*(n-2)+'*'
H(5)

# 16、打印出如图所示的杨辉三角形，要求可以自定义行数 
'''
1　                        1
2	                     1   1   
3	                   1   2   1   
4	                 1   3   3   1   
5	               1   4   6   4   1   
6	             1   5   10  10  5   1   
'''
def triangles(n):
    L = [1]
    count=1
    while count<n+1:
        print ' '*((2*n-1)-2*(count-1))+' '.join(str(x)+'  ' for x in L)
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
        count+=1
triangles(5)

# 17、打印如图所示图案，要求支持指定行数，但行数必须是奇数行
'''
*  
*  *  *  
*  *  *  *  *  
*  *  *  *  *  *  *  
*  *  *  *  *  
*  *  *  
*  
'''
def print_pic(n):
	for i in range(1,n+1):
		if i>n/2+1:
			i=n-(i-1)
		if 0<i<=n/2+1:
			print '*  '*(2*i-1)
print print_pic(7)

# 18、要求实现一函数，该函数用于求两个集合的差集，结果集合中包含 所有属于第一个集合但不属于第二个集合的元素 
def diff_set(seta,setb):
	for i in setb:
		if i in seta:
			seta.remove(i)
	return seta
seta=set([1,2,3,4])
setb=set((2,4,5,6))
print diff_set(seta,setb)

# 19、找出一段句子中最长的单词及其索引位置，以list返回 
s='All the fighters, landed safely on the airport after the military maneuver.'
max_word=''
for word in s.split():
	if word[-1] in ',.!?':
		len_word=len(word)-1
	else:len_word=len(word)
	if len_word>len(max_word):
		max_word=word
print max_word,s.split().index(max_word)+1

# 20、返回序列中的最大数
def get_max(seq):
	return max(seq)
print get_max([2,3,4,'f'])
######################
def get_max2(seq):
	for i in seq:
		if seq[0]<i:
			seq[0]=i
	return seq[0]


