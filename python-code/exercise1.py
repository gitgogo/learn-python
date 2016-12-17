#coding=utf-8
'''
Python课后练习题
'''
#1. 输入1-127的ASCII码输出对应字符
print chr(input('input 1-127 ascii: '))

#2. 输入a b c d4个整数，计算a+b-c*d的结果
a=input('input a integer: ')
b=input('input a integer: ')
c=input('input a integer: ')
d=input('input a integer: ')
print '%d+%d-%d*%d ='%(a,b,c,d),a+b-c*d

#3. 计算一周有多少分钟、多少秒
print u'一周有%d分钟，%d秒'%(7*24*60,7*24*3600)

#4. 3个人在餐厅吃饭，想分摊饭费。总共花费35.27美元，他们还想给15%的小费。每个人该怎么付钱，编程实现
print u'每个人应该平分%.2f美元'%(35.27*(1+0.15)/3)

# 5. 计算一个12.5m X 16.7m的矩形房间的面积和周长
area=12.5*16.7
perimeter=2*(12.5+16.7)
print u'房间的面积：%.2f平方米\n房间的周长：%.1f米'%(area,perimeter)
# 6. 怎么得到9 / 2的小数结果
print str(9.0/2).split('.')[-1]
# 7. python计算中7 * 7 *7 * 7，可以有多少种写法
print 7**4
print pow(7,4)
result=1
for i in range(4):
	result*=7
print result

# 8. 写程序将温度从华氏温度转换为摄氏温度。转换公式为C = 5 / 9*(F - 32)
F=input('input Fahrenheit：')
print '%.2fF = %.2fC '%(F,(5.0/9*(F - 32)))
# 9. 一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果
# 购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣(10%或20%)和
# 最终价格。
price=input('input your price:')
if 50<=price<=100:
	print u'享受%d%%折扣，实际需要支付%.2f元'%(10,(price*(1-0.1)))
elif price>100:
	print u'享受%d%%折扣，实际需要支付%.2f元'%(20,(price*(1-0.2)))
else:
	print u'不享受折扣，需要支付%.2f元'%price
# 10. 判断一个数n能否同时被3和5整除
n=input('input a number: ')
if not n%3 and not n%5:
	print 'Yes!'
else:
	print 'No!'
# 11.求1 + 2 + 3 +....+100
print reduce(lambda x,y:x+y,range(1,101))
sum=0
for i in range(1,101):
	sum+=i
print sum
# 12交换两个变量的值 
a,b=11,22
print 'before: a=%d,b=%d'%(a,b)
a,b=b,a
print 'after: a=%d,b=%d'%(a,b)
#13一个足球队在寻找年龄在10到12岁的小女孩(包括10岁和12岁)加入。编写一个程序，询问用户的性别(m表示男性，
# f表示女性)和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
count=0
for i in range(10):
	print u'第%d次输入'%(i+1)
	sex=raw_input('your gender: ')
	if sex.strip().lower()!='f':
		continue
	age=input('your age: ')
	if 10<=age<=12:
		print 'OK'
		count+=1
	else:
		print 'NO'
print '%d children is OK'%count

'''14 长途旅行中，刚到一个加油站，距下一个加油站还有200km，而且以后每个加油站之间距离都是200km。编写一个程
序确定是不是需要在这里加油，还是可以等到接下来的第几个加油站再加油。
程序询问以下几个问题:1)你车的油箱多大，单位升 2)目前油箱还剩多少油，按百分比算，比如一半就是0.5 3)你车每升油可以走多远(km)
提示:油箱中包含5升的缓冲油，以防油表不准。'''
capacity=input('capacity: ')
rest=input('remain: ')
distance=input('discover per liter: ')
a,b=divmod((capacity*rest*distance),200)
if a>0:
	print u'现在不需要加油，可以在第%d个加油站再加油'%a
else:
	print u'你现在必须加油'
# 15 现有面包、热狗、番茄酱、芥末酱以及洋葱，数字显示有多少种订购组合，其中面包必订，0不订，1订，比如10000， 表示只订购面包
count=0
for i in [0,1]:
	for j in [0,1]:
		for k in [0,1]:
			for h in [0,1]:
				count+=1
				print 1,i,j,k,h
print u'总共%d种订购组合'%count
# 16 基于上题:给出每种食物的卡路里(自定义)，再计算出每种组合总共的卡路里
bread,hotdog,tomato,musturd,onion=100,250,80,75,70
count=0
for i in range(2):
	for j in range(2):
		for k in range(2):
			for h in range(2):
				count+=1
				print '1%d%d%d%d = %d Colarie'%(i,j,k,h,100+250*i+80*j+75*k+70*h)
print u'总共%d种订购组合'%count
# 17输入5个名字，排序后输出
namelist=[]
for i in range(5):
	namelist.append(raw_input('input your name: '))
for nn in sorted(namelist):
	print nn,
namelist.sort()
print ' '.join(namelist)
''' 18实现一个简单的单词本 功能:
可以添加单词和词义，当所添加的单词已存在，让用户知道; 
可以查找单词，当查找的单词不存在时，让用户知道; 
可以删除单词，当删除的单词不存在时，让用户知道; 
以上功能可以无限制操作，直到用户输入bye退出程序。'''
bye=False
promp=u'''
这是一个简单的单词本，有以下几个功能：
输入【add】添加单词
输入【find】查找单词
输入【delete】删除单词
输入【bye】退出单词本
请选择输入：
'''
words=[]
while not bye:
	choice=raw_input(promp).strip().lower()
	if choice=='add':
		word=raw_input('input your word: ')
		if word in words:
			print '%s has been added'%word
		else: words.append(word)
	elif choice=='find':
		word=raw_input('input your word: ')
		if word not in words:
			print '%s not found'%word
		else: print 'Yes!'
	elif choice=='delete':
		word=raw_input('input your word: ')
		if word not in words:
			print '%s not found'%word
		else: 
			words.remove(word)
			print '%s has been deleted'%word
	elif choice=='bye':
		bye=True
#字典实现
#encoding=utf-8
wordsDict = {}
def addWord(word, meaning):
  if wordsDict.has_key(word):
    return False  
  wordsDict[word] = meaning
  
def findWord(word):
  if wordsDict.has_key(word):
    return wordsDict[word]
  return False
  
def delWord(word):
  if wordsDict.has_key(word):
    del wordsDict[word]
    return
  return False

def main():
  while 1:
    oper = raw_input("Add a word or look up a word or delete a word(a/l/d)")
    if oper.strip().lower() == "a":
      word = raw_input("Type the word: ").strip()
      meaning = raw_input("Type the definition: ").strip()
      res = addWord(word, meaning)
      if res is False:
        print "sorry, word has exists."
      else:
        print "succeed"
      continue
    elif oper.strip().lower() == "l":
      word = raw_input("look up the word: ").strip()
      res = findWord(word)
      if res is False:
        print "sorry, not exists."
      else:
        print "the definition:", res
      continue
    elif oper.strip().lower() == "d":
      word = raw_input("delete the word: ").strip()
      res = delWord(word)
      if res is False:
        print "sorry, not exists."
      else:
        print "succeed"
      continue
    elif oper.strip().lower() == "bye":
      exit()
    else:
      continue
      
if __name__ == "__main__":
  main()

# 19输入一个正整数，输出其阶乘结果
n=input('input your number: ')
print reduce(lambda x,y:x*y,range(1,n+1))
#递归方式
def facrorial(n):
	if n==1:
		return 1
	else:
		return factorial(n - 1) * n
#递归方式将字符串逆序输出
def fuc(s):
	if len(s)==1:
		return s
	else:
		return fuc(s[1:])+fuc(s[0])
print fuc('country')
# 20 计算存款利息 4种方法可选:
# 活期，年利率为r1; 一年期定息，年利率为r2; 存两次半年期定期，年利率为r3 两年期定息，年利率为r4
# 现有本金1000元，请分别计算出一年后按4种方法所得到的本息和。 提示:本息= 本金+ 本金* 年利率* 存款期
r1,r2,r3,r4=0.03,0.1,0.05,0.3
cash=1000
n1=cash*(1+r1)
n2=cash*(1+r2)
n4=cash*(1+r4*0.5)
for i in range(2):
	cash=cash+cash*r3*0.5
n3=cash
print u'四种方法的本息和为：',n1,n2,n3,n4
# 21输入3个数字，以逗号隔开，输出其中最大的数 
numbers=[]
for i in range(3):
	n=input('input a number: ')
	numbers.append(n)
print 'The biggest number is %d'%(sorted(numbers)[-1])
#two
def findMax(x,y,z):
	if x>y and x>z:
		return x
	elif y>z:
		return y
	else:return z

numList = raw_input("input 3 Integer: ").split(",")
print numList
res = findMaxNum(int(numList[0]), int(numList[1]), int(numList[2]))
print u"最大数是：", res
#冒泡排序
def bubbleSort(listnumber):
	n=len(listnumber)
	for i in range(n-1):
		for j in range(n-i-1):
			if listnumber[j]>listnumber[j+1]:
				listnumber[j],listnumber[j+1]=listnumber[j+1],listnumber[j]
	return listnumber
# 22输入一个年份，输出是否为闰年
# 是闰年的条件:能被4整数但不能被100整除，或者能被400整除的年份都是闰年。 
year=input('input a year: ')
if not year%4 and year%100 or not year%400:
	print u'%d 是闰年'%year
# 23求两个正整数m和n的最大公约数
m=input('input a number: ')
n=input('input a number: ')
for i in range(m/2,1,-1):
	for j in range(n/2,1,-1):
		if not m%i and not n%j and i==j:
			print u'最大公约数是',i
			break
#two辗转相除法

