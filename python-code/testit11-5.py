#coding=utf-8
'''调用一个给定函数，成功返回True及函数的返回结果,
失败返回False并打印错误信息,主要练习函数的参数调用，关键字参数、可变长参数
'''
def testit(func,*nkwargs,**kwargs):
	try:
		retval=func(*nkwargs,**kwargs)
		result=(True,retval)
	except Exception ,dialog:
		result=(False,str(dialog))
	return result

def test():
	funcs=(int,long,float)
	vals=(111,12.21,'1212','11.11')
	for eachFunc in funcs:
		print '--'*20
		for eachVal in vals:
			retval=testit(eachFunc,eachVal)
			if retval[0]:
				print '%s(%s)= '%(eachFunc.__name__ ,'eachVal'),retval[1]
			else:
				print '%s(%s)= FAILED'%(eachFunc.__name__ ,'eachVal'),retval[1]

if __name__=='__main__':
	test()