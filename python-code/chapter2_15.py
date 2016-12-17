#coding=utf-8
a=int(raw_input('input the first number: '))
b=int(raw_input('input the second number: '))
c=int(raw_input('input the third number: '))
if a>b:
	if c>a:
		print 'the sorted number is: %d,%d,%d'%(c,a,b)
	if c<b:
		print 'the sorted number is: %d,%d,%d'%(a,b,c)
elif a<b:
	if c<a:
		print 'the sorted number is: %d,%d,%d'%(b,a,c)
	if c>b:
		print 'the sorted number is: %d,%d,%d'%(c,b,a)