#coding=utf-8
#判断两个字符串是否相等
s1=raw_input('input the first str: ')
s2=raw_input('input the second str: ')
if len(s1)!=len(s2):
	print 'No!'
else:
	for i in range(len(s1)):
		if s1[i].lower()!=s2[i].lower():
			print 'No!'
			break
	else:
		print 'Yes!'
