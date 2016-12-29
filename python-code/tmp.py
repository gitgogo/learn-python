#coding=utf-8
import sys,os
def get_lines(file,num):
	try:
		with open(file) as f:
			for i,line in enumerate(f):
				if i<5:
					print line
				else:break
	except Exception,e:
		print e
get_lines('/Users/ralphliu/Document/learn-python/python-code/8-53.py',5)