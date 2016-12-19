#coding=utf-8
# 1、将一个正整数分解质因数 
def is_prime(num):
	for i in range(2,num/2):
		if not num%i:
			return False
	return True
lis=[]
def factori(num):
	global lis
	if is_prime(num):
		lis.append(num)
	else:
		for i in range(2,num):
			if not num%i:
				lis.append(i)
				return factori(num/i)
factori(24)
print lis
###
def func(x):
    listi=[]
    i=2
    while x>=2:
        if x%i==0 :
            listi.append(i)
            x=x/i
            print x
        else:
            i+=1          
    return listi
print func(90)
# 2、一个字符串中，分别输出奇数坐标字符或偶数坐标字符，奇数坐标的一行，偶数 坐标的一行
s='ohmygodthisisfunny'
odd_list=[]
even_list=[]
for i,j in enumerate(s,1):
	if i%2:
		odd_list.append(j)
	else:even_list.append(j)
print ' '.join(odd_list)
print ' '.join(even_list)
# 3、统计字符串中的字母、数字、其他字符个数 
s='ohmy1 2,r4. #$isisfunny'
def count_str(s):
	digit=char=other=0
	for i in s:
		if i.isdigit():
			digit+=1
		if i.isalpha():
			char+=1
		else:
			other+=1
	return digit,char,other
print count_str(s)
# 4、有一个已经排好序的列表。现输入一个数，要求按原来的规律将它插入列表中 
def insertNum(lis,num):
	list_tmp=lis[:]
	for i in lis:
		if i>=num:
			list_tmp.insert(list_tmp.index(i),num)
			return list_tmp
print insertNum([4,6,7,23,45,67,123],28)

'''
一个长度15个字符的字符串，顺序读取字符，
第一次打印1一个，第二次打印2个，第三次打印三个。。。
类推，打印5个，如果到结尾，则从开头继续打印。注意每个字符只打印一次
'''
s='abcdefghijklmn'
s1=s[:]
i=1
while i<9:
	if len(s1)<i:
		s1=s1+s
	print s1[:i]
	s1=s1[i:]
	i+=1

# 5、统计名字列表中，各名字的首字母在名字列表中出现的次数
name_list=['lisi','wangwu','liutao','wuyun','sunqian']
name_f=[x[0] for x in name_list]
name_dict=dict.fromkeys(name_f,0)
for x in name_f:
	name_dict[x]+=1
for name,count in name_dict.items():
	print name,count

'''
6、字符替换
1)读入一个字符串；2)去掉字符串的前后空格； 
3)如果字符串包含数字则1替换成a，2替换成b，3替换成c，以此类推 
4)将字符串使用空格进行切分，存到一个列表，然后使用*号连接，并输出 
5)把这些功能封装到一个函数里面，把执行结果作为返回值
'''
from string import maketrans
def strange(strr):
	strr=strr.strip()
	tran=maketrans('123456789','abcdefghi')
	trans_str=strr.translate(tran)
	list_tmp=trans_str.split()
	return '*'.join(list_tmp)
# 7、找出字符串中出现次数最多的字符，并输出其出现的位置 
def get_most_char(strr):
	most_char=['',0]
	tmp=set(list(strr))
	for i in tmp:
		if strr.count(i)>most_char[1]:
			most_char[0]=i
			most_char[1]=strr.count(i)
	tmp_list=[]
	while strr.find(most_char[0])!=-1:
		tmp_list.append(strr.find(most_char[0]))
		strr=strr.replace(most_char[0],' ',1)
	return most_char,tmp_list
	
# 8、找出一段句子中最长的单词及其索引位置，以字典返回
from string import maketrans
def get_longest_word(strr):
	trans=maketrans(',.?!','    ')
	strr=strr.translate(trans)
	word_list=strr.split()
	result={}
	for word in word_list:
		result[word]=word_list.index(word)
	return sorted(result.items(),key=lambda x:len(x[0]))[-1]
strr='''Trumps going to get us into war because he can't stop tweeting. Can't someone take this 8 year old man boy's phone away for the safety of our country?'''
print get_longest_word(strr)
'''
9、字母游戏
“Pig Latin”是一个英语儿童文字改写游戏，整个游戏遵从下述规则:
(1). 元音字母是‘a’、‘e’、‘i’、‘o’、‘u’。字母‘y’在不是第一个字母的情况下，也被视作元音 字母。
其他字母均为辅音字母。例如，单词“yearly”有三个元音字母(分别为‘e’、‘a’和最后一个 ‘y’)和三个辅音字母(第一个‘y’、‘r ’和‘l’)。
(2). 如果英文单词以元音字母开始，则在单词末尾加入“hay”后得到“Pig Latin”对应单词。
例如，“ask” 变为“askhay”，“use”变为“usehay”。(同上)
(3). 如果英文单词以‘q’字母开始，并且后面有个字母‘u’，将“qu”移动到单词末尾加入“ay”后得到 “Pig Latin”对应单词。
例如，“quiet”变为“ietquay”，“quay”变为“ayquay”。
(4). 如果英文单词以辅音字母开始，所有连续的辅音字母一起移动到单词末尾加入“ay”后得到“Pig Latin” 对应单词。
例如，“tomato”变为“omatotay”， “school” 变为“oolschay”，“you” 变为 “ouyay”，“my” 变为“ymay ”，“ssssh” 变为“sssshay”。
(5). 如果英文单词中有大写字母，必须所有字母均转换为小写。
输入格式:
一系列单词，单词之间使用空格分隔。
输出格式:
按照以上规则转化每个单词，单词之间使用空格分隔。
输入样例:
Welcome to the Python world Are you ready
输出样例:
elcomeway otay ethay ythonpay orldway arehay ouyay eadyray
'''
def pig_latin(word):
	word=word.lower()
	if word[0] in 'aeiou':
		return word+'hay'
	if word[:2]=='qu':
		return word[2:]+'quay'
	if word[0] not in 'aeiou':
		for i in range(1,len(word)):
			if word[i] in 'aeiouy':
				return word[i:]+word[:i]+'ay'
def to_pig_latin(sentance):
	tmp_list=sentance.split()
	for i in range(len(tmp_list)):
		tmp_list[i]=pig_latin(tmp_list[i])
	return ' '.join(tmp_list)
# 10、实现字符串的upper、lower以及swapcase方法
def my_upper(strr):
	tmp=''
	for s in strr:
		if 97<=ord(s)<=122:
			tmp+=chr(ord(s)-32)
		else:tmp+=s
	return tmp
print my_upper('Oh Yeah!4')

def my_lower(strr):
	tmp=''
	for s in strr:
		if 65<=ord(s)<=90:
			tmp+=chr(ord(s)+32)
		else:tmp+=s
	return tmp
print my_lower('OH My God4')
# 11、实现字符串的find方法
def my_find(strr,s):
	for i,j in enumerate(strr):
		if j==s:
			return i
print my_find('hello','o')
# 12、实现字符串的isalpha方法
def my_isalpha(strr):
	for i in strr:
		if not (97<=ord(i)<=122 or 65<=ord(i)<=90):
			return False
	return True
# 13、实现字符串的isdigit方法
def my_isdigit(strr):
	for i in strr:
		if not 48<=ord(i)<=57:
			return False
	return True
# 14、实现字符串的isalnum方法
def my_isalnum(strr):
	for i in strr:
		if not (my_isdigit(strr) or my_isalpha(strr)):
			return False
	return True
# 15、实现字符串的join方法
def my_join(seq,strr=''):
	tmp=''
	for i in seq:
		try:
			tmp+=i+strr
		except TypeError:
			print 'the seq must be str'
			break
	if len(strr)==0:
		return tmp
	else:return tmp[:-len(strr)]
print my_join(['a','d','c'],'*')
# 16、实现字符串的replace方法
def my_replace(strr,src,str_replace):
	result=''
	while src in strr:
		index=strr.find(src)
		result+=strr[:index]+str_replace
		strr=strr[index+len(src):]
	return result+strr
print my_replace('addcddbddedd','dd','**')
# 17、实现字符串的split方法
def my_split(strr,str_split):
	result=[]
	while str_split in strr:
		index=strr.find(str_split)
		result.append(strr[:index])
		strr=strr[index+len(str_split):]
	result.append(strr)
	return result
print my_split('addcddbddedd','dd')
# 18、实现字符串的strip方法 
def my_strip(strr,str_strip=' '):
	for i,j in enumerate(strr):
		if j!=str_strip:
			result=strr[i:]
			break
	tmp=result[::-1]
	# my_strip(tmp,str_strip=' ')
	for i,j in enumerate(tmp):
		if j!=str_strip:
			result1=tmp[i:]
			break
	return result1[::-1]
print my_strip('aaagda bsaa','a')
# 19、报数问题:有n个人围成一圈，顺序排号。从第一个人开始报数(从1到3报数) ，凡报到3的人退出圈子，问最后留下的是原来第几号的那位 

# 20、由单个字母组成的list，从键盘读入两个整数m、n(n>m)，打印出list[m,n]之间 的字母能组成的所有n-m+1位不同的字符串



