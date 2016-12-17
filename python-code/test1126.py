#coding=utf-8
lis=[1,2,3,8,8,3,8,4,8]
while 8 in lis:
	lis.remove(8)
print lis

#遍历多维数组
def fn(lis):
	global lii
	for i in lis:
		if not isinstance(i,list):
			lii.append(i)
		else:
			fn(i)
	return lii
lii=[]
lis=[1,2,3,[5,6,[8,9,0],7]]
print fn(lis)

import copy  
a = [1, 2, 3, 4, ['a', 'b']] #原始对象  
  
b = a #赋值，传对象的引用  
c = copy.copy(a) #对象拷贝，浅拷贝  
d = copy.deepcopy(a) #对象拷贝，深拷贝  
  
a.append(5) #修改对象a
a[4].append('c') #修改对象a中的['a', 'b']数组对象
  
print 'a = ', a  
print 'b = ', b  
print 'c = ', c  
print 'd = ', d 
