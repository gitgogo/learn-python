#coding=utf-8
import os
ls=os.linesep

while True:
	filename=raw_input('input filename: ')
	if os.path.exists(filename):
		print '%s already exists'%filename
	else:
		break

all=[]
print '\nEnter lines("." to quit):\n '
while True:
	entry=raw_input('input your contents=== ')
	if entry=='.':
		break
	else:
		all.append(entry)

with open(filename,'w') as f:
	f.writelines(['%s%s'%(s,ls) for s in all])
