#coding=utf-8
'''小于1美元的的金额最少能换多少枚硬币'''
def fun(m):
	m=m*100
	if m%25==0:
		print '%.2f dollar ---- %d 25cents'%(m/100,m/25)
	elif m%25%10==0:
		print '%.2f dollar ---- %d 25cents and %d 10cents'%(m/100,m/25,m%25/10)
	elif m%25%10%5==0:
		print '%.2f dollar ---- %d 25cents and %d 10cents and %d 5cents'%(m/100,m/25,m%25/10,m%25%10/5)
	else:
		print '%.2f dollar ---- %d 25cents and %d 10cents and %d 5cents and %d 1cents'%(m/100,m/25,m%25/10,m%25%10/5,m%25%10%5)	

if __name__ == '__main__':
	m=float(raw_input('input money: '))
	fun(m)
