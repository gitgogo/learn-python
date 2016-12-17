#coding=utf-8
#计算语句中每个字母的个数
s='from random import randrange'
dict_s={}
for i in s:
	if i.isalpha():
		dict_s[i]=s.count(i)
print dict_s
#读写文件
f=open('f:\\1.txt','w')
j=0
for i in range(1,101):
	f.write(str(i)+' '+chr(97+j)+'\n')
	j+=1
	if j>25:
		j=0
f.close()