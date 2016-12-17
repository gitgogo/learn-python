#coding=utf-8
#打印斐波那契数列的第n个数
def Fibonacci(n):
	a=b=1
	for i in range(n-1):
		a,b=b,a+b
	return a
n=input('input number: ')
print Fibonacci(n)