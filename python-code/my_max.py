#max内建函数
def my_max(*args):
	maxs=0
	if len(args)==1:
		for j in args[0]:
			if j>maxs:
				maxs=j
	elif len(args)>1:
		for i in range(len(args)):
			if args[i]>maxs:
				maxs=args[i]
	return maxs

print my_max([1,2,3],4,3)