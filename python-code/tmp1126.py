#coding=utf-8
from random import randrange
# lis=sorted([randrange(100) for _ in range(15)])
f=open('f:\\1.txt','w')
j=0
for i in range(1,101):
	f.write(str(i)+' '+chr(97+j)+'\n')
	j+=1
	if j>25:
		j=0
f.close()


