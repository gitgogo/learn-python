#coding=utf-8
# import random

for i in range(5):
	guess_number=random.randrange(1,11)
	input_number=input('猜数字： '.decode('utf-8').encode('gbk'))
	i+=1
	if input_number<guess_number:
		print u'小了'
	elif input_number>guess_number:
		print u'大了'
	elif input_number==guess_number: 
		print u'恭喜！猜对了！'
		break
	print u'还有%d次机会'%(5-i)
	if i==5:
		print u'没机会了，正确答案是 ',guess_number

for i in range(10000):
    a=i+1
    b=i+1
    if id(a)!=id(b):
        print i
        break

#随机生成12位密码
#第一种--------------------
from random import *
passwd=''
for j in range(12):
	s1=chr(randint(48,57))
	s2=chr(randint(65,91))
	s3=chr(randint(97,122))
	passwd=passwd+choice([s1,s2,s3])
print passwd
#第二种--------------------
import string
# password=''
all=string.ascii_letters+string.digits
# for i in sample(all,12):#想要将列表中的元素组合成字符串用join
# 	password+=i
print ''.join(sample(all,12))#注意join的使用
#short
import string
print ''.join(sample(string.ascii_letters+string.digits,12))
#--------------------------
#去除多余的空格
' '.join("Please n don't    t hurt x0b me.".split())
#随机生成10个135-139之间的手机号
for i in range(10):
	print randint(13500000001,13999999999)

#-------------------
import pdb
phone='13'
n1=randint(5,9)
for i in range(9):
	n2=randint(0,9)
	pdb.set_trace()#在此处暂停
	phone=phone+str(n2)
print phone