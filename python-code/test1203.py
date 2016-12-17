#coding=utf-8
# a=(1,2,3,2,2)
# b=('a','s','d')
# lis=[]
# for i in a:
# 	lis.append(i)
# for j in b:
# 	lis.append(j)
# t=tuple(lis)
# print t

# def traversal(seq):
# 	for i in seq:
# 		if isinstance(i,(tuple,list)):
# 			for j in i:
# 				print j,
# 			print
# traversal([2,3,[2,3,4],(3,'d'),4,5])
# #匿名函数
# map(lambda x:','.join([i for i in x]),filter(lambda x:isinstance(x ,(list,tuple)),new_zoo))

# dict1={'name': 'ralph', 'sex': 'male'}
# def find_keys(val):
# 	for i in dict1.items():
# 		if val in i:
# 			return i[0]
# print find_keys('male')

# book_shelf={'1988':'HH','qingnian':'HH','qilixiang':'jay','zhu':'wangXiaoBo'}
# for i,j in book_shelf.items():
# 	print j,i
# print u'所有书名：',','.join(book_shelf.keys())
# print u'所有作者：',','.join(list(set(book_shelf.values())))

user={'user13':'a1c','user2222':'c1a','userw1':'bw'} 
sort=sorted(user.items(),key=lambda e:e[1][-1],reverse=False)   #排序
# print sort
# print type(sort)
for item in sort:
    print "%s= %s"  %(item[0],item[1])
