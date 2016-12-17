#coding=utf-8
#返回一个整形的所有约数8-5
def getfactors(n):
	l=[]
	for i in range(1,n+1):
		if n%i==0:
			l.append(i)
	return l

n=input('input a number: ')
print getfactors(n)

#8-6素因子分解
def factors(n):
	l2=[]
	for i in getfactors(n):
		if isprime(i) and i!=1:
			l2.append(i)
	for j in l2:
		if 