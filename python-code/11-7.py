#coding=utf-8
#使用map函数实现zip功能

def to_zip(list1,list2):
	list0=[]
	for i in range(len(list2)):
		list0.append(tuple([list1[i],list2[i]]))
	return map(lambda x:x,list0)
print to_zip([1,2,3],['d','r','w'])