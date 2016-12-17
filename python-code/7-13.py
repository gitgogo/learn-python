#coding=utf-8
import random
listA=[]
listB=[]
for i in range(10):
	listA.append(random.randint(0,9))#randint包含起始、末尾值
	listB.append(random.randrange(0,10))#randrange包含起始值、不包含末尾值
A=set(listA)
B=set(listB)

print A|B ,A&B