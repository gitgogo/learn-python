#coding=utf-8
#判断一个数是否完全数，一个数的约数之和等于它本身
# def isperfect(n):
# 	l=[]
# 	for i in range(1,n):
# 		if n%i==0:
# 			l.append(i)
# 	if sum(l)==n: return 1
# 	else: return 0
# #判断一个数是否完全数
# n=input('input a number: ')
# print isperfect(n)
# #打印1000以内所有的完全数
# for i in range(1,1001):
# 	if isperfect(i):
# 		print i,

#8-8计算一个数的阶乘
def factorial(n):
	result=1
	for i in range(1,n+1):
		result*=i
	return result
n=input('input a number: ')
print factorial(n)