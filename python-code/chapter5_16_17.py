#coding=utf-8
# def payment(balance,payment):
# 	print 'Pymt#	Paid	Balance'
# 	print '-----	-----	-----'
# 	i=0
# 	while balance>=0:
# 		print '%d 	$ %.2f	$ %.2f'%(i,payment,balance)
# 		i+=1
# 		balance-=payment

# # payment(100.00,16.13)
# if __name__ == '__main__':
# 	balance=input('Enter opening balance: ')
# 	payment=input('Enter monthly payment: ')
# 	payment(balance,payment)#TypeError: 'int' object is not callable

import random
i,j=1,1
l,c=[],[]
while i<=random.randint(1,101):
	x=random.randint(0,2**31)
	l.append(x)
	i+=1
while j<=random.randint(1,101):
	y=random.choice(l)
	c.append(y)
	j+=1
print c