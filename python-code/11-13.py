#coding=utf-8
#reduce实现阶乘
def mult(x,y):
	return x*y
print reduce(mult,range(1,6))
#递归方式
def mm(n):
	if n==1 or n==0:
		return 1
	else:
		return n*mm(n-1)
print mm(5)