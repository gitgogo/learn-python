#coding=utf-8
'''计算器程序'''
def calc(n1,o,n2):
	if o=='+':
		return n1+n2
	elif o=='-':
		return n1-n2
	elif o=='*':
		return n1*n2
	elif o=='/':
		return n1/n2
	elif o=='%':
		return n1%n2
	elif o=='**':
		return n1**n2

if __name__=='__main__':
	n1=input('input the first number: ')
	o=raw_input('input the operator: ')
	n2=input('input the second number: ')
	print calc(n1,o,n2)