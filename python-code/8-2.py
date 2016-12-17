#coding=utf-8
#判断一个数是否素数
def isprime(n):
	for i in range(2,n):
		if n%i==0:
			return False
			break
		else:return True

while True:
	n=input('input a number: ')
	print isprime(n)
	if n==0:
		break