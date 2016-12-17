#coding=utf-8
# def chang(list1):
# 	list1.append('newstr')
# 	print list1

# list1=[1,2,3]
# print list1
# chang([1,2,3])
# print list1

# # def add_end(L=[]): #调用会出错
# def add_end(L=None):
# 	if L is None:
# 		L=[]
# 	L.append('END')
# 	return L

# print add_end([1,2,3])
# print add_end(['x','y','z'])
# print add_end()
# print add_end()
# print add_end()

# def summ(*t):
# 	result=0
# 	for i in t:
# 		result+=i
# 	return result
# print summ(1,2,3,3)

# def sum1(**kw):
# 	summ=0
# 	for val in kw.values():
# 		summ+=val
# 	return summ
# print sum1(a=1,b=3,c=4)

# def sum(a,b=3,*args,**kw):
# 	result=0
# 	for i in args:
# 		result+=i
# 	for j in kw.values():
# 		result+=j
# 	return result+a+b
# print sum(2,1,3,4,w=3,f=2)
# from functools import partial

# def repeat(n):
# 	return lambda s:s*n
# twice=repeat(2)
# print twice('world__')
# print twice(5)
# print repeat(3)('God-!')

# def sum(a,b):
# 	return a+b

# import string

# filter(lambda x:x if x in string.lowercase else '','HJjhWsG')
#递归实现阶乘运算
def fn(n):
	if n==1:
		return 1
	else:
		return n*fn(n-1)
print fn(5)
#斐波那契数列第n项数，递归实现
def fabo(n):
	if n==1:
		return 0
	elif n==2:
		return 1
	else:
		return fabo(n-1)+fabo(n-2)
print fabo(7)