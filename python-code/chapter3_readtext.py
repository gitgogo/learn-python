#coding=utf-8

filename=raw_input('input your filename: ')
print '-*-*-*-*-*-*-*-*-*-*-*-*-*-*-'
#the first way
# with open(filename,'r') as f:
# 	for line in f:
# 		print line,

#the second way,use try-except-else
try:
	f=open(filename,'r')
except IOError ,e:
	print 'file open error: ',e
else:
	for line in f:
		print line.strip()
	f.close()