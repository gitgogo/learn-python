#coding=utf-8
# 14、按如下规律打印列表 
# 1 [1*, 2, 3, 4, 5]
# 2 [1, 2*, 3, 4, 5]
# 3 [1, 2, 3*, 4, 5]
# 4 [2, 3, 4*, 5, 6] 
# 5 [3, 4, 5*, 6, 7] 
# 6 [4, 5, 6*, 7, 8] 
# ...
# 20 [16, 17, 18, 19, 20*]
k=g=1
for i in range(1,8):
	if i%2:
		for j in range(3):
			print g,[x for x in range(1,k*5+1)][-5:]
			g+=1
		k+=1
	else:
		for h in range(1,4):
			print g,[x for x in range(1,i/2*5+1+h)][-5:]
			g+=1
