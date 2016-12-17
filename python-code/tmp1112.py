#coding=utf-8
# m=input('input a number: ')
# n=input('input a number: ')
# for i in range(m/2,1,-1):
# 	for j in range(n/2,1,-1):
# 		if not m%i and not n%j and i==j:
# 			print u'最大公约数是',i
# 			break
'''
程序实现算法步骤：
第一步：r = a % b
第二步：(1)if r == 0, return b;
        (2)elif a, b = b, r; r = a % b
第三步：重复第二步中的(2)，直到r == 0，return b
按照上面步骤完成后返回的b就是所要的结果
'''
# a=25
# b=30
# def fuc(a,b):
# 	while not a%b:
# 		r=a%b
# 		if not r:
# 			return b
# 		else:
# 			a,b=b,r
# 			r=a%b
# 			return b
# print fuc(a,b)
# def char_Calc(listWord) :
# 	dictChar = {}
#   #判断首字母是否在字典中存在，如存在value+1，不存在将value=1
#   for i in listWord :
#     if dictChar.has_key(i[0]) :
#     	dictChar[i[0]] += 1
#     else :
#     	dictChar[i[0]] = 1
#     return dictChar

# name=['foster','foe','lily','mickel','live','moon','ruby','cindy','miya']
# dictStatistics = char_Calc(name)
# for i, j in dictStatistics.items() :
# 	print u"姓名以字母 %s 开头的有 : %d人" %(i,j)

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