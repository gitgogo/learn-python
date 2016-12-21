#coding=utf-8
with open('f:\\1.txt') as f:
	for i,j in enumerate(f):
		if i%2:
			print j