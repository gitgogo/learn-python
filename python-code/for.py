
summ=0
for i in range(3):
	n=raw_input('input a number: ')
	try:
		n=float(n)
		summ=summ+n
		print summ
	except Exception,e:
		print e

for i in range(1,11):
	print i

for i in range(2,11):
	if i%2==1:
		print i
