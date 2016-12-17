#coding=utf-8
import string
import keyword
alpha=string.letters+'_'
num=string.digits

myIput=raw_input('input your letter to test: ')
if myIput[0] not in alpha:
	print 'Invalid '
elif myIput in keyword.kwlist:
	print 'keyword is not used'
else:
	for other in myIput[1:]:
		if other not in alpha+num:
			print 'Invalid'
			break
	else:
		print 'Okay,It is right.'