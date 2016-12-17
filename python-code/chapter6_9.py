#coding=utf-8
minu=input('input minutes: ')
if minu/60>=1:
	print '%dH%dM'%(minu/60,minu%60)
else:
	print '%dM'%minu