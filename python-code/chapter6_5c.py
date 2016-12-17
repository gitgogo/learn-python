#coding=utf-8
#判断一个字符串是否重现
s=raw_input('input your str: ')
first=[]
for i in range(len(s)):
	if s[i] not in first:
		first.append(s[i])
	else:
		print '%s is repeated'%s[i]
	i+=1
if len(first)==len(s):
	print 'no one is repeated'