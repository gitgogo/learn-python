#coding=utf-8

# 1.使用尽可能多的方法实现list去重
#one
l=[1,1,1,2]
print list(set(l))
#two
list1=[]
for i in l:
	if not i in list1:
		list1.append(i)
print list1
#three
for i in l:
	if l.count(i)>1:
		l.remove(i)
#four
dict2=dict.fromkeys(l,0)
print dict2.keys()
# 2.成绩等级判断
# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，
# 60-89分之间的用B表示，60分以下的用C表示
# score=input('请输入你的分数(0-100)：'.decode('utf-8').encode('gbk'))
# if score>=90:
# 	print '%.1f:A'%score
# elif 60<=score<=89:
# 	print '%.1f:B'%score
# elif score<60:
# 	print '%.1f:C'%score
# else:
# 	print u'输入不合法'
# 3.实现数学中多项式求和公式的打印
# 比如：a6x^6 + a5x^5 + a4x^4 + a3x^3 + a2x^2 + a1x^1 + a0
an=[1,2,3,4,5,6]
x=2
summ=0
for i in range(len(an)):
	summ+=an[i]*x**i
print summ

#coding=utf-8
def multinomial(a, n, x) :
  mathStr = ''
  i = n
  while i >= 0 :
    if i == 0 :
      mathStr += a + "0"
    else :
      mathStr += a + str(i) + x + "^" + str(i) + " + " 
    i -= 1
  return mathStr
print multinomial('a', 8, 'x')
####
def multinomial(a, n, x) :
  mathStr = ''
  i = n
  while i >= 0 :
    if i == 0 :
      mathStr += a + "0"
    else :
      mathStr += a + str(i) + x + "^" + str(i) + " + " 
    i -= 1
  return mathStr

# 4.统计名字列表中，各名字的首字母在名字列表中出现的次数
namelist=['wang','liu','lu','wu','li','zhang']
name_first=[]
for name in namelist:
	first=name[0]
	name_first.append(first)
name_first1=list(set(name_first))
print u'所有不重复的名字首字母有%d个'%len(name_first1)
for i in name_first1:
	print i,name_first.count(i)
#字典方法
def char_count(listWord):
	dictChar={}
	for i in listWord:
		if dictChar.has_key(i[0]):
			dictChar[i[0]]+=1
		else:
			dictChar[i[0]]=1
	return dictChar

name=['foster','foe','lily','mickel','live','moon','ruby','cindy','miya']
dictStatistics=char_count(name)
for i,j in dictStatistics.items():
	print u'姓名以字母%s开头的有%d人'%(i,j)

# 5.输入三个数，判断是否能构成三角形
# 能构成三角形三边关系：
# 三边都大于零
# 两边之和大于第三边，两边之差小于第三边
def is_tangle(a,b,c):
	if a>0 and b>0 and c>0:
		list1=sorted([a,b,c])
		if list1[0]+list1[1]>list1[2]: #and list1[2]-list1[0]<list1[1]:
			return True
		else: return False
	else: return False
print is_tangle(3,4,5)
####answer
def check_triangle(a, b, c):
  if a <= 0 or b <= 0 or c <= 0:
    return False 
  flag = a + b > c and a + c > b and b + c > a
  if not flag:
    return False 
  return True 

if __name__ == '__main__':
  while True:
    print u"========== 请输入三角形的三边边长(a, b, c) ==========="
    a = int(raw_input('a = '))
    b = int(raw_input('a = '))
    c= int(raw_input('a = '))
    print check_triangle(a, b, c)

# 6.实现字典的fromkeys方法,例如：
# seq = ('name', 'age', 'sex')
# dict = dict.fromkeys(seq, 10)
# print "New Dictionary : %s" % str(dict)
# 结果：New Dictionary : {'age': 10, 'name': 10, 'sex': 10}
def my_fromkeys(seq,s):
	my_dict={}
	for key in seq:
		my_dict[key]=s
	return my_dict
print my_fromkeys(('name','age','sex'),12)

# 7.键盘读入一字符串，逆序输出
print raw_input('输入一串字符：'.decode('utf-8').encode('gbk'))[::-1]
#two
s=raw_input('input your string: ')
l=list(s)
l.reverse()
''.join(l)
# 8.读入一个整数n，输出n的阶乘
# print reduce(lambda x,y:x*y,range(1,input('input a number: ')+1))
# 9.打印1/2, 1/3, 1/4,….1/10
def fraction(n):
	for i in range(2,n+1):
		print '1/%d,'%i,
fraction(10)

# 10.写一个函数实现一个数学公式
#例如：1,3,5,7,9……（2n-1)。等差数列的通项公式为：an=a1+(n-1)d。
#前n项和公式为：Sn=n*a1+n(n-1)d/2或Sn=n(a1+an)/2
def SN(a1,d,n):
	an=a1+(n-1)*d
	summ=0
	for number in range(a1,an+1,d):
		summ+=number
	return summ
print SN(1,1,100)

# 11.输入数字a，n，如a，4，则打印a+aa+aaa+aaaa之和
def func(a,n):
	list_number=[]
	for i in range(n):
		an=0
		for j in range(i+1):
			an+=a*10**j
		list_number.append(an)
	return sum(list_number)
print func(2,4)
#two
246=200+20*2+2*3  (2,3)

# 12.求100个随机数之和，随机数要求为0—9的整数
from random import randint
num_list=[]
for i in xrange(100):
	num_list.append(randint(0,9))
print num_list,sum(num_list)

# 13.要求在屏幕上分别显求1到100之间奇数之和与偶数之和
#one
odd_number=[]
even_number=[]
for i in xrange(1,101):
	if i%2:
		odd_number.append(i)
	else:even_number.append(i)
print u'1-100的奇数之和：%d\n1-100的偶数之和：%d'%(sum(odd_number),sum(even_number))
#two
print sum([x for x in xrange(1,101,2)])
print sum([x for x in xrange(0,101,2)])

# 14.输入10个数，并显示最大的数与最小的数
list_number=[]
for i in range(10):
	list_number.append(input('input a number: '))
list_number.sort()
print u'最大值：%d\t最小值：%d'%(list_number[-1],list_number[0])

# 15.给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出
# 各位数字。
# def number_count():
# 	n=input('input a number(less than 5): ')
# 	for i in range(6):
# 		sub=n/(10**i)
# 		if not sub:
# 			count=i
# 			break
# 		else:print u'各位数字逆序输出：',(n/10**i)%10,
# 	return count
# print number_count()
def number_c(number):
	count=0
	while number:
		count+=1
		# print number%10,
		number=number/10
	return count
print number_c(12345)

# 16.求所有的水仙花数:水仙花数是指一个 n 位数 ( n≥3 )，
# 它的每个位上的数字的 n 次幂之和等于它本身。
# （例如：1^3 + 5^3+ 3^3 = 153）
# for number in range(100,1000):
# 	digit=number%10
# 	tens=number/10%10
# 	hun=number/100
# 	if digit**3+tens**3+hun**3==number:
# 		print number,

n=100
while n<1000000:
	n+=1
	summ=0
	count=len(str(n))
	for i in range(count):
		summ+=pow((n/10**i)%10,count)
	if summ==n:
		print n
#map
#encoding=utf-8
import math

def myPow(n):
  return int(math.pow(int(n), 3))

for i in xrange(100, 1000):
  res = sum(map(myPow, list(str(i))))
  if res == i:
    print i

			
# 17.编程求s=1!+2!+3!+…..+n!
def multisum(n):
	summ=0
	for num in range(1,n+1):
		mul=reduce(lambda x,y:x*y,range(1,num+1))
		summ+=mul
	return summ
print multisum(4)

# 18.钞票换硬币
# 把一元钞票换成一分、二分、五分硬币（每种至少一枚），有多种换法，分
# 别有哪些？
count=0
for i in range(1,101):
	for j in range(1,51):
		for h in range(1,21):
			if i+2*j+5*h==100:
				count+=1
				print u'%d 个1分+ %d个2分+ %d个5分'%(i,j,h)
print u'总共 %d 种换发'%count

# 19.自己实现在一句话中查找某个单词的算法，存在返回索引号，否则返回
# False
sentence='He pines for kindness, as well as love and a kind word from you would be his best medicine'
word='love'
# def find_word(sentence,word):
# 	sentence_list=sentence.split()
# 	for i in range(len(sentence_list)):
# 		print sentence_list[i],
# 		if word == sentence_list[i]:
# 			return i
# 			break
# 		else:
# 			return False
# print find_word(sentence,word)
sentence_list=sentence.split()
sentence_list.index('for')

def find_word(sentence,word):
	for i in range(len(sentence)):
		count=0
		for j in range(len(word)):
			if word[j]==sentence[i+j]:
				count+=1
			else:continue
		if count==len(word):
			return i,sentence[i:i+len(word)]
			break
print find_word(sentence,word)

# 20.读入一个十进制整数，实现十进制转二进制算法将其转成二进制数
# 要求：不能使用现成进制转换函数，自己写代码实现
def ten_to_bin(n):
	binstr=''
	while n:
		binstr+=str(n%2)
		n=n/2
	return binstr[::-1]
print ten_to_bin(12)