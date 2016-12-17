#encoding=utf-8
# print u"中国"
'''输入得分：
如果>=90,打印优
'''
i=0
while i<3:
	i+=1
	score=int(raw_input('请输入你的分数： '.decode('utf-8').encode('gbk')))
	if score>=90 and score<=100:
		print u'优'
	elif score<90 and score>=80:
		print u'良'
	elif score<80 and score>=70:
		print u'中'
	elif score<70 and score>60:
		print u'及格'
	elif score==60:
		print u'跳出循环'
		break
	elif score<0 or score>100:
		print u'输入不合法'
	else:
		print u'不及格'

# a,i=1,0
# while i<5:
# 	a+=a
# 	i+=1
# 	print a


