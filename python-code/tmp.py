#coding=utf-8
import sys
import random
week={'m':'monday','t':'tuesday','w':'wednesday','t':'Thursday','f':'Friday','s':{'a':'Saturday','u':'sunday'}}
s=raw_input('input an alpha->').lower()
if s in week.keys() and s!='s':
	print week[s]
elif s=='s':
	s1=raw_input('input the second alpha->').lower()
	if s1 in 'au':
		print week['s'][s1]
	else:
		print 'invalid!'
else:
	print 'invalid!'