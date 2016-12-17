#coding=utf-8
n=10
while n>0:
	n-=1
	print n

for i in range(10):
	print i,

for asci in range(65,91):
	print chr(asci),

#遍历元素
t = [1,24,[3,4,5],('a','b','c'), 8, 9]
for i in t:
	if isinstance(i,(list,tuple)):
		for j in i:
			print j,
		print #换行
	else:
		print i
#索引遍历
for i in range(len(t)):
	if isinstance(t[i],(list,tuple)):
		for j in t[i]:
			print j,
		print
	else:print i
#嵌套循环
for i in range(5):
	for j in range(5):
		for k in range(5):
			print k,
		print
	print
#嵌套循环输出10-50中个位带有1-5的所有数字
#one
for i in range(10,51):
	for j in range(1,6):
		if i%10==j:
			print i,
#two
for i in range(10,51):
	if i%10 in range(1,6):
		print i,

#直接退出多重循环
class getoutofloop(Exception): pass
try:
	for i in range(5):
		for j in range(5):
			for k in range(5):
				if i == j == k == 3:
					raise getoutofloop()
				else:
					print i, '----', j, '----', k
except getoutofloop:
	pass
#直接退出多重循环
for i in range(5):
	for j in range(5):
		for k in range(5):
			if i == j == k == 3:
				break
			else:
				print i, '----', j, '----', k
		else: continue
		break
	else: continue
	break