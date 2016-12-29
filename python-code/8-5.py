#coding=utf-8
#返回一个整形的所有约数8-5
def getfactors(n):
	l=[]
	for i in range(1,n+1):
		if n%i==0:
			l.append(i)
	return l
#test it
# n=input('input a number: ')
print getfactors(12)
print type(getfactors(12))