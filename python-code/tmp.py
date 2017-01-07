#coding=utf-8
import sys
import random
def is2power(n):
	while n>1:
		print n
		if n%2:
			return False
		n=float(n)/2
	else:
		return True
print is2power()