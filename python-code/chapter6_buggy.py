#coding=utf-8
num=input('Enter a number: ')
fac_list=range(1,num+1)
print 'Before: ',fac_list
i=0
while i<len(fac_list):
	if num%fac_list[i]==0:
		del fac_list[i]
		i=i-1 #bug fix
	i=i+1
print 'After: ',fac_list