#coding=utf-8
#输出对应数字的英文表示
n=raw_input('input a number: ')
num=['1','2','3','4','5','6','7','8','9','10']
eng=['one','two','three','four','five','six','seven','eight','nine','ten']
two=['']
if len(n)==1 or n=='10':
	print '%d: %s'%(int(n),eng[num.index(n)])
elif len(n)==2 and n!='10':
	print '%d: %s-%s'%(int(n),eng[num.index(n[0])],eng[num.index(n[1])])