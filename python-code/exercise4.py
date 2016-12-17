#coding=utf-8
# 练习题1:操作一个list做增删该查操作(写一个图书管理系统)

# 练习题2:完成引用复制和非引用复制的一个例子 
a=[2,3,1,'e',['a','s']]
b=a#引用赋值
c=a[:]#非引用赋值
import copy
d=copy.copy(a)#浅拷贝，不拷贝['a','s']
e=copy.deepcopy(a)#深拷贝连同['a','s']

# 练习题3:找到两个列表中不同的元素和相同元素 
def same_diff_list(lis1,lis2):
	lis_same,lis_diff=[],[]
	for i in lis1:
		if i in lis2:
			lis_same.append(i)
	lis_diff=list(set(lis1)-set(lis2))+list(set(lis2)-set(lis1))
	return lis_same,lis_diff
#直接使用set操作
# lis_diff=list(set(lis1)^set(lis2))
# lis_same=list(set(lis1)&set(lis2))

# print same_diff_list([1,2,3,4],[3,4,8])
# print same_diff_list([1,3,4],[3,4,8])
# print same_diff_list([1,2,3,4],[3,4,8,4,6])
# 练习题4:数字和字母混合的list中，奇数位加1，偶数为加2 
lis=[2,'r','s',3,5,'y']
for i in range(len(lis)):
	if i%2:
		if isinstance(lis[i],int):
			lis[i]+=1
		else:lis[i]+=str(1)
	else:
		if isinstance(lis[i],int):
			lis[i]+=2
		else:lis[i]+=str(2)
# print lis
# 练习题5:递归处理嵌套的list 
def handle_list(lis):
	for i in lis:
		if isinstance(i,(list,tuple)):
			handle_list(i)
		else:
			print i,
# handle_list([1,4,3,[2,3],[4,5,['w','e',[4,5]]],8])
# 练习题6:遍历list，但是list中元素的数据类型不定，有可能有嵌套的list，嵌套的tuple，dict等

# 练习题7: 通过遍历list去掉重复部分 
def del_dup(lis):
	for i in lis:
		if lis.count(i)>1:
			lis.remove(i)
	return lis
# print del_dup([2,3,2,2,5,3])
# 练习题8:1个纯数字的list中，分别输出奇数坐标字符或偶数坐标字符 
range(0,9,2)
range(1,9,2)
# 练习题9:找到序列中最大的元素
def get_max(seq):
	for i in seq:
		if seq[0]<i:
			seq[0]=i
	return seq[0]

# 练习题10:返回列表中第二大元素
# sorted(seq)[-2]

#练习题11:键盘读入一字符串，逆序输出
# print raw_input('input your string: ')[::-1]

# 1、从键盘输入两个数，并比较其大小，直到输入e/E退出程序 
while True:
	num_list=raw_input("'input two numbers with ',' split ").lower().split(',')
	if num_list[0]=='e':
		break
	else:print 'the bigger is %s'%sorted(num_list,key=int)[-1]
# 2、请写一个函数，第一个参数为一个字母，另外一个参数为一个数字n，请返回这个字母后的第n个字母，
#如果达到字母表的末尾，则从头开始选取字母 
def fun(s,n):
	if s.isupper():
		s=s.lower()
		if ord(s)+n>122:
			return chr(ord(s)+n-122+97-1).upper()
		else:return chr(ord(s)+n).upper()
	else:
		if ord(s)+n>122:
			return chr(ord(s)+n-122+97-1)
		else:return chr(ord(s)+n)

# 3、分别输出字符串中奇数坐标和偶数坐标的字符
import string
string.lowercase[0::2]
string.lowercase[1::2]

# 4、输出杨辉三角形
def yang_hui(n):
	num=[1]
	i=0
	while i<n:
		print ' '*((2*n-1)-2*(i-1))+' '.join(str(x)+'  ' for x in num)
		num.append(0)
		num=[num[x]+num[x-1] for x in range(len(num))]
		i+=1
yang_hui(6)

# 5、将一个多重嵌套的列表的元素进行互换，存到另一个同等维度的嵌套列表中，例如: [[1,2,3],[4,5,6]]互换后变成[[1,4],[2,5],[3,6]]
def swap_list(lis):
	result=[]
	for i in range(len(lis)-1):
		for j in range(len(lis[i])):
			result.append(list((lis[i][j],lis[i+1][j])))
	return result
swap_list([[1,2,3],[4,5,6],[7,8,9]])

# 6、有一个3 x 4的矩阵，要求编程求出其中值最大的那个元素的值，以及其所在的行号和 列号，矩阵可以通过嵌套列表来模拟
from random import randrange
lis=[]
for i in range(3):
	lis1=[]
	for j in range(4):
		num=randrange(100)
		print num,
		lis1.append(num)
	lis.append(lis1)
	print
maxnum=0
lisij=[]
for i in range(3):
	for j in range(4):
		if maxnum<lis[i][j]:
			maxnum=lis[i][j]
			lisij.append(i)
			lisij.append(j)
print u'如上矩阵中最大数为%d，位于矩阵的第%d行，第%d列'%(maxnum,lisij[-2]+1,lisij[-1]+1)

# 7、递归实现列表求和
def sum_list(lis):
	if len(lis)==1:
		return lis[0]
	else:
		return sum_list(lis[0])+sum_list(lis[1:])
print sum_list([1,2,3,4,5])
# 8、打印斐波拉契数列前n项 
def fib(n):
	if n==1:
		return 0
	elif n==2:
		return 1
	else:
		return fib(n-2)+fib(n-1)
print fib(5)
# 9、检查ipV4的有效性，有效则返回True，否则返回False 
def is_ipv4(s):
	try:
		ip_list=[int(x) for x in s.split('.')]
	except ValueError:
		print 'must be integer'
		return False
	print ip_list
	if len(ip_list)!=4:
		return False
	for i in ip_list:
		if i>255 or i<0:
			return False
		else:return True
print is_ipv4('10.211.67.21')

# 10、检测密码强度
# c1 : 长度>=8
# c2: 包含数字和字母
# c3: 其他可见的特殊字符
# 强:满足c1,c2,c3
# 中: 只满足任一2个条件 弱:只满足任一1个或0个条件
def c1(s):
	if len(s)>=8:
		return True
	else:return False
def c2(s):
	flag1=flag2=False
	for char in s:
		if char.isdigit():
			flag1=True
		if char.isalpha():
			flag2=True
	if flag1 and flag2:
		return True
	else:return False
def c3(s):
	for i in s:
		if i in string.punctuation:
			return True
		else:return False
def check_passwd(s):
	if c1(s) and c2(s) and c3(s):
		print u'强'
	else:
		pass

# 11、返回列表中第二大元素
lis=[randrange(100) for x in range(10)]
print sorted(set(lis))[-2]
#方法2
lis_set=set(lis)
lis_set.remove(max(lis))
max(lis_set)

# 12、已知一字符串列表list1 = ['a','b','c','d', 'e', 'f', 'g']，对序列的任一子序列list1[start, end] 
# 中的元素进行排列组合，有多少种不同的组合，请分别输出。(start >= 0, end < len(list1))

# 13、判断一个字符串是否为回文字符串
# 所谓回文字符串，就是一个字符串，从左到右读和从右到左读是完全一样的。比如 "level" 、 “aaabbaaa”
def is_symmetry(s):
	if s[:len(s)/2]==s[-(len(s)/2):][::-1]:
		return True
	else:
		return False
# 14、实现合并同类型的有序列表算法，要求不能有重复元素 

# 15、有4个圆锥塔，圆心分别为(20, 20)、(-20, 20)、(-20, -20)、(20，-20)， 圆半径为10m，见下图。
# 这4个塔的高度为100m，塔以外无建筑物。今输入任一点坐标， 
# 求该点的建筑高度(塔外的高度为0)，结果不需要特别精确，只需要考虑坐标为整数的 情况

# 16、一个数如果恰好等于它的因子之和，这个数就称为完数，例如6的因子为1,2,3，而 6=1+2+3，因此6是完数，
# 编程找出1000之内的所有完数，并按6 its factors are 1,2,3这 样的格式输出
for i in range(1,1001):
	lis=[]
	for j in range(1,i):
		if not i%j:
			lis.append(j)
	if sum(lis)==i:
		print '%d its factors are %s'%(i,','.join([str(x) for x in lis]))

# 17、使用二分法实现在一个有序列表中查找指定的元素 
lis=sorted([randrange(100) for _ in range(15)])
def find(num):
	global lis
	while lis:
		target=lis[len(lis)/2]
		if len(lis)==1 and num!=target:
			return False
			break
		if num==target:
			return True
			break
		elif num>target:
			lis=lis[len(lis)/2:]
		else:
			lis=lis[:len(lis)/2]
print find(15)
# 18、分离list1与list2中相同部分与不同部分 
set(list1)&set(list2)
set(list1)^set(list2)
# 19、找出一个多维数组的鞍点，即该位置上的元素在该行上最大，在该列上最小，也可 能没有鞍点
is=[[1,3,180,2],[2,1,19,3],[3,4,170,2],[2,3,100,1]]
for i in range(len(lis)):
	maxi=max(lis[i])
	indexi=lis[i].index(maxi)
	list_column=[]
	for j in range(len(lis)):
		list_column.append(lis[j][indexi])
	minj=min(list_column)
	if list_column.index(minj)==i:
		print minj,list_column
# 20、写一个函数，识别输入字符串是否是符合 python 语法的变量名
from string import letters,digits
def is_python(s):
	if s[0] not in '_'+letters:
		return False
	for i in s[1:]:
		if i not in '_'+letters+digits:
			return False
	return True
print is_python('_few22')

